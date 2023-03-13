class Solution():
	integer_to_lexems = [',', '.', 'Ten', 'green bottle', 's',
	                     'hanging on the wall', 'And', 'if', 'one',
	                     'should accidentally fall',
	                     'There`ll be', 'nine', 'Nine', 'eight', 'One',
	                     'If', 'that', 'no']

	@staticmethod
	def print_third_seven_lines() -> None:
		integer_to_lexems = Solution.integer_to_lexems
		print(
			f"{integer_to_lexems[6]} {integer_to_lexems[7]}"
			f" {integer_to_lexems[8]} "
			f"{integer_to_lexems[3]} {integer_to_lexems[9]}"
			f"{integer_to_lexems[0]}")

	@staticmethod
	def solve() -> None:
		integer_to_lexems = Solution.integer_to_lexems
		print(2 * f"{integer_to_lexems[2]} {integer_to_lexems[3]}"
		          f"{integer_to_lexems[4]} "
		          f"{integer_to_lexems[5]}{integer_to_lexems[0]}\n", end='')
		Solution.print_third_seven_lines()
		print(
			f"{integer_to_lexems[10]} {integer_to_lexems[11]} "
			f"{integer_to_lexems[3]} "
			f"{integer_to_lexems[4]}{integer_to_lexems[5]}"
			f"{integer_to_lexems[1]}")
		print(
			2 * f"{integer_to_lexems[12]} {integer_to_lexems[3]}"
			    f"{integer_to_lexems[4]} "
			    f"{integer_to_lexems[5]}{integer_to_lexems[0]}\n", end='')
		Solution.print_third_seven_lines()
		print(f"{integer_to_lexems[10]} {integer_to_lexems[13]} "
		      f"{integer_to_lexems[3]}{integer_to_lexems[4]} "
		      f"{integer_to_lexems[5]}{integer_to_lexems[1]}")
		print(3 * f"{integer_to_lexems[1]}")
		print(2 * f"{integer_to_lexems[14]} {integer_to_lexems[3]} "
		          f"{integer_to_lexems[5]}{integer_to_lexems[0]}\n", end='')
		print(f"{integer_to_lexems[-3]} {integer_to_lexems[-2]} "
		      f"{integer_to_lexems[8]} {integer_to_lexems[3]} "
		      f"{integer_to_lexems[9]}")
		print(f"{integer_to_lexems[10]} {integer_to_lexems[-1]} "
		      f"{integer_to_lexems[3]}{integer_to_lexems[4]} "
		      f"{integer_to_lexems[5]}{integer_to_lexems[1]}")


if __name__ == '__main__':
	Solution.solve()
