def solve(filename: str) -> None:
	result = dict()
	with open(filename, 'r') as file:
		for line in file:
			lexems = line.replace(',', '').split()
			for word in lexems[2:]:
				result[word] = result[word] + [
					lexems[0]] if word in result.keys() else [lexems[0]]
	result = dict(sorted(result.items()))
	for key, values in result.items():
		print(key, '-', ', '.join(value for value in values))


if __name__ == '__main__':
	print("Please, print a filename.")
	solve(str(input()))
