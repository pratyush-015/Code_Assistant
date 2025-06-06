import os

EXCLUDED_DIRS = {
    ".git", "node_modules", "dist", "build", "__pycache__", "venv", "logs",
    ".vscode", ".idea", ".next", ".turbo", "tmp", "temp", ".pytest_cache", "child1",
}

EXCLUDED_EXTS = {
    ".jpg", ".png", ".svg", ".ico", ".exe", ".dll", ".zip", ".tar", ".gz",
    ".pyc", ".log", ".tmp", ".bak", ".db", ".sqlite", ".mp3", ".mp4",
}

BASE_DIR = os.path.abspath(
    r"C:\Users\tanbi\door\hall_projects\medVault\MedVault" # this is just a placeholder this must be static for every instance of the program
    # TODO: write script which retrives the user's projects base URL and then update this BASE_DIR constant.
)


