#!/usr/bin/env python3

import sys
from pathlib import Path

# Returns list of tuples containing information about files and their sizes
def list_files(dir: Path) -> list[tuple[str, int]]:
    return [(entry.name, get_size(entry)) for entry in dir.iterdir()]

# Returns full size of file or directory
def get_size(file: Path) -> int:
    if file.is_file():    # Edge case for recursion
        return file.stat().st_size
    return sum([get_size(entry) for entry in file.iterdir()])    # Recursively calculate size for each subdirectory

# Used as entrypoint
if __name__ == '__main__':
    for file_info in sorted(list_files(Path(sys.argv[1])), key = lambda file_info: (-file_info[1], file_info[0])):
        print(f'{file_info[1]:<7d} {file_info[0]}')
