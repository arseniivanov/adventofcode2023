from utils.file_reader import read_all_lines

import re

def find_first_last_digit(s):
    word_to_digit = {
        'zero': '0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4',
        'five': 'f5e', 'six': 's6', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
    }

    pattern = '|'.join(word_to_digit.keys())

    modified_string = re.sub(pattern, lambda x: word_to_digit[x.group()], s)
    modified_string = re.sub(pattern, lambda x: word_to_digit[x.group()], modified_string)

    digits = [char for char in modified_string if char.isdigit()]

    if digits:
        return int(digits[0] + digits[-1])
    else:
        return None

x = sum(map(find_first_last_digit, read_all_lines("input")))
print(x)    