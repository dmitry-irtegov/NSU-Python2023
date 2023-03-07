import os
import sys


def joiner(dirpath: str, path: str) -> str:
	return os.path.join(dirpath, path)


def solve(dirpath: str) -> None:
	data = os.listdir(dirpath)
	files = [(value, os.stat(joiner(dirpath, value)).st_size) for value in
	         data if os.path.isfile(joiner(dirpath, value))]
	files = sorted(files, key=lambda file: file[0])
	files = sorted(files, key=lambda file: -file[1])
	print(*files)


if __name__ == '__main__':
	solve(sys.argv[1])
