import os
import uuid
from typing import Optional
from dataclasses import dataclass

@dataclass
class CodeChunk:
    id: str
    file_path: str
    filename: str
    content: str
    start_line: int
    end_line: int
    tokens: int
    language: str
    chunk_type: Optional[str]
    metadata: Optional[dict] = None

    @classmethod
    def from_raw_data(cls,
                     file_path: str,
                     content: str,
                     start_line: int,
                     end_line: int,
                     tokens: int,
                     language: str,
                     chunk_type: Optional[str],
                     metadata: Optional[dict] = None):
        filename = os.path.basename(file_path)
        generated_id = str(uuid.uuid4())

        if language is None:
            ext = os.path.splitext(filename)[1]
            language = cls._infer_language_from_extension(ext)

        return cls(
            id=generated_id,
            file_path=file_path,
            filename=filename,
            content=content,
            start_line=start_line,
            end_line=end_line,
            tokens=tokens,
            language=language,
            chunk_type=chunk_type,
            metadata=metadata
        )

    @staticmethod
    def _infer_language_from_extension(ext: str) -> str:
        return {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.html': 'html',
            '.css': 'css',
        }.get(ext.lower(), 'unknown')