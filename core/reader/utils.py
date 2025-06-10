import os
import json
import tiktoken

def get_encoder(model="gpt-3.5-turbo"):
    return tiktoken.encoding_for_model(model)

def serialize_data(chunker_instance):
    """
    returns serialized data object for valid json dumps
    """
    serialized_data = [{"id": data.id,
    "file_path": data.file_path,
    "filename": data.filename,
    "content": data.content,
    "start_line": data.start_line,
    "end_line": data.end_line,
    "tokens": data.tokens,
    "language": data.language,
    "chunk_type": data.chunk_type,
    "metadata": data.metadata} for data in chunker_instance.GlobalChunks]

    return serialized_data

def write_file(file_path, content):
    with open("data.json", "w") as f:
        json.dump(content, f, indent=1)