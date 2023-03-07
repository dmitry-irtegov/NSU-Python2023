number: int = int(input('Enter a number to check: '))

while True:
    print(number, end='')
    if number == 1:
        break
    number = number // 2 if number % 2 == 0 else 3 * number + 1
    print('->', end='')
