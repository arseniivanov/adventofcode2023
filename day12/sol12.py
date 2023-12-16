import numpy as np

def read_input_file(file_path):
    """Reads the input from the file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def parse_input(lines):
    nonograms = []
    for line in lines:
        pattern, clues = line.split()
        clues = [int(num) for num in clues.split(',')]  # Convert clues to integers
        nonograms.append((pattern, clues))
    return nonograms

fp = "input"
f = read_input_file(fp)
nonogram_clues = parse_input(f)

from functools import cache

def generate_combinations(pattern, clues):
    def is_valid(comb, clues):
        idx, count, clue_idx = 0, 0, 0
        while idx < len(comb):
            if comb[idx] == '#':
                count += 1
            elif count > 0:
                if clue_idx >= len(clues) or clues[clue_idx] != count:
                    return False
                clue_idx += 1
                count = 0
            idx += 1
        if count > 0:
            if clue_idx >= len(clues) or clues[clue_idx] != count:
                return False
            clue_idx += 1
        return clue_idx == len(clues)

    def backtrack(index, current):
        if index == len(pattern):
            if is_valid(current, clues):
                results.append(''.join(current))
            return
        if pattern[index] != '?':
            backtrack(index + 1, current + [pattern[index]])
        else:
            backtrack(index + 1, current + ['#'])
            backtrack(index + 1, current + ['.'])

    results = []
    backtrack(0, [])
    return results

tot_combs = 0
for line, clues in nonogram_clues:
    combinations = generate_combinations(line, clues)
    tot_combs += len(combinations)

print(tot_combs)
