def read_schematic(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def is_symbol(char):
    return char not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_adjacent_indices(schematic, start_x, end_x, y):
    adjacent_indices = set()

    # Check the cells directly above and below each digit in the number
    for x in range(start_x, end_x + 1):
        for dy in [-1, 1]:
            adj_y = y + dy
            if 0 <= adj_y < len(schematic[0]):
                adjacent_indices.add((x, adj_y))

    # Check the ends and diagonals at the ends of the number
    for dx in [-1, 1]:
        adj_x = start_x + dx if dx == -1 else end_x + dx
        if 0 <= adj_x < len(schematic):
            adjacent_indices.add((adj_x, y))
            for dy in [-1, 1]:
                adj_y = y + dy
                if 0 <= adj_y < len(schematic[0]):
                    adjacent_indices.add((adj_x, adj_y))

    return adjacent_indices

def find_non_adjacent_numbers(schematic):
    non_adjacent_numbers = []
    y = 0
    while y < len(schematic):
        x = 0
        while x < len(schematic[y]):
            if schematic[y][x].isdigit():
                start_x = x
                while x < len(schematic[y]) and schematic[y][x].isdigit():
                    x += 1
                number = int("".join(schematic[y][start_x:x]))
                adjacent_indices = get_adjacent_indices(schematic, start_x, x - 1, y)
                if any(is_symbol(schematic[adj_y][adj_x]) for adj_x, adj_y in adjacent_indices):
                    non_adjacent_numbers.append(number)
            else:
                x += 1
        y += 1
    return non_adjacent_numbers

schematic = read_schematic("input")
non_adjacent_numbers = find_non_adjacent_numbers(schematic)
print(sum(non_adjacent_numbers))

from functools import reduce

def find_gears_and_calculate_ratio(schematic):
    gear_ratios = []

    def find_full_number(schematic, x, y):
        # Find the start of the number
        while x > 0 and schematic[y][x-1].isdigit():
            x -= 1
        # Capture the full number
        number = ''
        while x < len(schematic[y]) and schematic[y][x].isdigit():
            number += schematic[y][x]
            x += 1
        return int(number) if number else None

    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if schematic[y][x] == '*':
                part_numbers = set()
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue
                        adj_x, adj_y = x + dx, y + dy
                        if 0 <= adj_x < len(schematic[y]) and 0 <= adj_y < len(schematic) and schematic[adj_y][adj_x].isdigit():
                            number = find_full_number(schematic, adj_x, adj_y)
                            if number is not None:
                                part_numbers.add(number)
                if len(part_numbers) == 2:
                    gear_ratios.append(reduce(lambda a, b: a * b, part_numbers))

    return sum(gear_ratios)

# Use the existing 'read_schematic' function to read the schematic
schematic = read_schematic("input")
total_gear_ratio = find_gears_and_calculate_ratio(schematic)
print(total_gear_ratio)

