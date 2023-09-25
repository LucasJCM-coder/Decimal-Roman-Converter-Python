#!/bin/python3
import sys
from typing import Union


def get_input() -> str:
    command_line_argument = '--input-file='
    argument_receives = sys.argv[1:]

    is_file_input = any(command_line_argument in arg_value for arg_value in argument_receives)

    if is_file_input:
        file_path = argument_receives.pop().split('=')[1]
    elif sys.stdin.isatty():
        file_path = " ".join(argument_receives)
    else:
        file_path = f"/proc/self/fd/{sys.stdin.fileno()}"

    with open(file_path) as file:
        input_data = file.read().strip()

    return input_data


def number_to_roman(num: Union[str, int]) -> str:
    num = int(num)
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_value = ''
    while num > 0:
        for key in roman_numerals:
            if num - key < 0:
                continue
            roman_value += roman_numerals[key]
            num -= key
            break

    return roman_value


def roman_to_number(letter_roman: str) -> int:
    symbol_roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def calculate_roman_to_number_rule(value, next_value):
        return -value if next_value > value else value

    roman_to_integer = list(map(lambda x: symbol_roman[x], letter_roman))
    signal_rules = [calculate_roman_to_number_rule(value, next_value) for value, next_value in
                    zip(roman_to_integer, roman_to_integer[1:] + [0])]

    return sum(signal_rules)


def choice_function(input_value: str) -> str:
    result = number_to_roman(input_value) if input_value.isnumeric() else str(roman_to_number(input_value))
    return f'{input_value} => {result}'


def read_multiple_lines(input_data: str) -> str:
    return '\n'.join([choice_function(line) for line in input_data.split('\n')])


def main():
    input_data = get_input()
    output = read_multiple_lines(input_data) if '\n' in input_data else choice_function(input_data)

    print(output)


if __name__ == '__main__':
    main()
