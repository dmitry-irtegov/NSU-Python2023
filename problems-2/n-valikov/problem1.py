def solve(n: int) -> [(int, int, int)]:
	n += 1
	return [(x, y, z) for x in range(1, n) for y in range(x, n) for z in
	        range(y, n) if x ** 2 + y ** 2 == z ** 2]


if __name__ == '__main__':
	print("Please, print a number.")
	print(solve(int(input())))
