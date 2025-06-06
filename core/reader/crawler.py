import os
from config import EXCLUDED_DIRS, EXCLUDED_EXTS, BASE_DIR
from state import VALID_FILES_CONTAINER

def crawl_for_valid_files(base_dir):
    """
        crawls the codebase and selects only the valid files to read
    """
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS and not d.startswith('.')]

        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in EXCLUDED_EXTS or file.startswith('.'):
                continue
            path = os.path.join(root, file)
            VALID_FILES_CONTAINER.append(path)
