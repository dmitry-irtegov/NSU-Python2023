#!/usr/bin/env python3

quantities: list[str] = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']    # Numbers as strings

# Used as entrypoint
if __name__ == '__main__':
    for i in range(10, 0, -1):
        if i == 1:
            print(f'{quantities[i].capitalize()} green bottle hanging on the wall,\n' * 2, end = '')
            print('If that one green bottle should accidentally fall,')
        else:
            print(f'{quantities[i].capitalize()} green bottles hanging on the wall,\n' * 2, end = '')
            print('And if one green bottle should accidentally fall,')
        print(f'There’ll be {quantities[i - 1]} green bottles hanging on the wall.')
