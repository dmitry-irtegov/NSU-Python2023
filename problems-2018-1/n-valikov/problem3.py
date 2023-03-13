import math
import time

import bitarray


def sieve_of_Eratosthenes_list(N: int):
	numbers_list = [number for number in range(N)]
	for index in range(2, int(N ** 0.5) + 1):
		if numbers_list[index] > 0:
			numbers_list[index * 2:N:index] = [-1] * (
				math.ceil((N - index * 2) / 1.0 / index))
	return [number for number in numbers_list[2:] if number > 0]


def sieve_of_Eratosthenes_set(N: int):
	numbers_set = {number for number in range(2, N)}
	for number in range(2, int(N ** 0.5) + 1):
		if number in numbers_set:
			for deletion_number in range(number * 2, N, number):
				if deletion_number in numbers_set:
					numbers_set.remove(deletion_number)
	return numbers_set


def sieve_of_Eratosthenes_bitarray(N: int):
	numbers_bitarray = bitarray.bitarray('1' * N)
	numbers_bitarray[0:2] = 0
	for index in range(2, int(N ** 0.5) + 1):
		if numbers_bitarray[index]:
			numbers_bitarray[index * 2:N:index] = 0
	return [number for number in range(2, N) if numbers_bitarray[number]]


if __name__ == '__main__':
	N: int = 100000000
	N += 1
	start_time: float = time.time()
	sieve_of_Eratosthenes_list(N)
	print(f'List: {time.time() - start_time}s')
	start_time: float = time.time()
	sieve_of_Eratosthenes_set(N)
	print(f'Set: {time.time() - start_time}s')
	start_time: float = time.time()
	sieve_of_Eratosthenes_bitarray(N)
	print(f'Bitarray: {time.time() - start_time}s')
