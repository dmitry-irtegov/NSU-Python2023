def solve(array: [int], lower_bound: int, upper_bound: int) -> [int]:
	result = list(filter(lambda number: lower_bound <= number <= upper_bound,
	                     array))
	return result


if __name__ == '__main__':
	print("Please, print an array of numbers.")
	array = list(map(int, input().split()))
	print("Please, print a lower bound.")
	lower_bound = int(input())
	print("Please, print an upper bound.")
	upper_bound = int(input())
	print(solve(array, lower_bound, upper_bound))
