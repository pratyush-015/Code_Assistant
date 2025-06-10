# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ..reader import crawl_for_valid_files, chunker, serialize_data
from ..config import BASE_DIR
import json
from ..state import VALID_FILES_CONTAINER

def run_test():
    # extracting valid files to read
    crawl_for_valid_files(BASE_DIR)

    # creating instance of the chunker
    code_chunker = chunker()

    for i, file_path in enumerate(VALID_FILES_CONTAINER):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"# chunking {i} ...")
        code_chunker.lineChunker(content=content, file_path=file_path, max_tokens=400, overlap_tokens=10)

    serialized_data = serialize_data(code_chunker)
    with open("data.json", "w") as f:
        json.dump(serialized_data, f, indent=1)

run_test()






