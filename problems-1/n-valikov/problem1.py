def solve(input_array: [int]) -> [int]:
	result = [0]
	adder = lambda result_array, number: result_array + [
		result_array[-1] + number]
	for number in input_array:
		result = adder(result, number)
	return result


if __name__ == '__main__':
	print("Please, write numbers in one line.")
	print(solve(list(map(int, input().split()))))
