def is_prime(n: int) -> bool:
	if n % 2 == 0:
		return False
	for number in range(3, int(n ** 0.5) + 1, 2):
		if n % number == 0:
			return False
	return True


def solve(n: int) -> [int]:
	return [2] + [number for number in range(3, n + 1, 2) if is_prime(number)]


if __name__ == '__main__':
	print("Please, print a number.")
	print(solve(int(input())))
