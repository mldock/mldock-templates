"""
    FILE UTILS

    A set of utils to format files correctly.
    i.e. set correct executable permissions.
"""

from pathlib import Path, PosixPath

def find_files(base_path: str, regexp: str):
    return list(Path(base_path).glob(regexp))

def set_file_permissions_executable(files: list):
    """sets file permissions to be executable"""
    if not isinstance(files, list):
        raise TypeError("Expected files to be of type 'list'.")

    for file_ in files:
        if not isinstance(file_, PosixPath):
            file_ = Path(file_)
        file_.chmod(0o777)

if __name__ == '__main__':

    bases = ["dev/base", "prod/base"]
    for base_path in bases:
        files = find_files('dev/base', regexp='*/**/executor.sh')
        set_file_permissions_executable(files)
