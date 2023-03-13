def finder(index: int, count: int, pattern: str, data: str) -> (int, int):
	return data.find(pattern, index + 1), count + 1


def solve(pattern: str) -> (int, [int]):
	count = 0
	results = []
	with open('pi.txt', 'r') as file:
		data: str = file.read()[2:]
		index = -1
		for i in range(5):
			index, count = finder(index, count, pattern, data)
			results += [index]
			if index == -1:
				break
		while index < len(data) and index != -1:
			index, count = finder(index, count, pattern, data)
	return count, results


if __name__ == '__main__':
	print("Enter sequence to search for.")
	answer = solve(str(input()))
	print(f"Found {answer[0]} results.")
	print(f"Positions: {answer[1]}")
