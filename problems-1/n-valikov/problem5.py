def solve(number: int) -> [[int, int]]:
	if number == 1:
		return [[1, 1]]
	result = []
	power = 0
	while number % 2 == 0:
		number //= 2
		power += 1
	if power > 0:
		result += [[2, power]]
		power = 0
	for i_number in range(3, int(number ** 0.5), 2):
		while number % i_number == 0:
			number //= i_number
			power += 1
		if power > 0:
			result += [[i_number, power]]
			power = 0
	if number != 1:
		result += [[number, 1]]
	return result


if __name__ == '__main__':
	print("Please, print a number.")
	print(solve(int(input())))
