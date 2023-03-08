#!/usr/bin/env python3

import sys

# Converts dictionary from the specified file and writes it to the given one
def convert_dictionary(input_file: str, output_file: str) -> None:
    dictionary: dict[str, list[str]] = {}
    with open(input_file, 'r') as file:
        for mapping in file:
            source, _, destination = mapping.partition('-')
            destination: list[str] = destination.split(',')
            for word in destination:
                dictionary[word.strip()] = dictionary.get(word.strip(), []) + [source.rstrip()]
    with open(output_file, 'w') as file:
        for key, value in sorted(dictionary.items()):
            file.write(f'{key} - {", ".join(value)}\n')

# Used as entrypoint
if __name__ == '__main__':
    convert_dictionary(sys.argv[1], sys.argv[2])
