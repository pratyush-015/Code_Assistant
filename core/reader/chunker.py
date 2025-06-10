from .utils import get_encoder
from .config import MAX_TOKENS, OVERLAP_TOKENS
from .codechunk import CodeChunk

encoder = get_encoder() # default model -> gpt-3.5-turbo

class chunker():
    def __init__(self, enc=encoder, max_tokens=MAX_TOKENS, overlap_tokens=OVERLAP_TOKENS):
        self.GlobalChunks = []
        self.MAX_TOKENS = max_tokens
        self.OVERLAP_TOKENS = overlap_tokens
        self.enc = enc
    
    def count_tokens(self, text):
        return len(self.enc.encode(text))
    
    # TODO: start line, end line bug not fixed. [i fixed it, i guess]
    def lineChunker(self,
                    content,
                    file_path,
                    max_tokens=None,
                    overlap_tokens=None):
        
        lines = content.splitlines()
        # chunks = [] rather store in GLobalChunks
        current_chunks = []
        current_tokens = 0
        token_count = [self.count_tokens(line+"\n") for line in lines]
        i=0

        while i < len(lines):
            # print(i)
            line = lines[i]
            line_tokens = token_count[i]
            # print(line_tokens, current_tokens)

            if line_tokens > max_tokens:
                
                start_line = i+1
                end_line = start_line + len(current_chunks)-1;
                if current_chunks:
                    # create the structured data of the current chunks data
                    chunk_content = "\n".join(current_chunks)
                    data = CodeChunk.from_raw_data(
                        file_path=file_path,
                        content=chunk_content,
                        start_line=start_line,
                        end_line=end_line,
                        tokens=current_tokens,
                        language=None,
                        chunk_type= None# dont know what to do here
                    )
                    
                    # store it to GLobalChunks
                    self.GlobalChunks.append(data)
                    
                    # reset current chunkers and current token counter
                    current_chunker = []
                    current_tokens = 0
                # create the structured data of the long line
                line_content = "\n".join(line)
                data = CodeChunk.from_raw_data(
                        file_path=file_path,
                        content=line_content,
                        start_line=i+1,
                        end_line=i+1,
                        tokens=token_count[i],
                        language=None,
                        chunk_type= None# dont know what to do here
                    ) 
                # store it to GLobalChunks
                self.GlobalChunks.append(data)
                i+=1
                continue

            if current_tokens + line_tokens > max_tokens:
                start_line = i+1 - len(current_chunks)
                end_line = i

                # create the structured data of the current chunks data
                chunk_content = "\n".join(current_chunks)
                data = CodeChunk.from_raw_data(
                        file_path=file_path,
                        content=chunk_content,
                        start_line=start_line,
                        end_line=end_line,
                        tokens=current_tokens,
                        language=None,
                        chunk_type= None# dont know what to do here
                    )
                # store it to GlobalChunks
                self.GlobalChunks.append(data)

                overlap_lines = current_chunks[-overlap_tokens:] if overlap_tokens else []
                current_chunks = overlap_lines.copy()
                start_idx = i - len(overlap_lines)
                current_tokens = sum(self.count_tokens(l + "\n") for l in current_chunks)
            else:
                current_chunks.append(line)
                current_tokens+=line_tokens
                i+=1
        if current_chunks:
            start_line = i+1 - len(current_chunks)
            end_line = i 
            # create the structured data of the current chunks data
            chunk_content = "\n".join(current_chunks)
            data = CodeChunk.from_raw_data(
                        file_path=file_path,
                        content=chunk_content,
                        start_line=start_line,
                        end_line=end_line,
                        tokens=current_tokens,
                        language=None,
                        chunk_type= None# dont know what to do here
                    )
            # store it to GlobalChunks
            self.GlobalChunks.append(data)
        
    
    def makeChunks(self):
        pass
