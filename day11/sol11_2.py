import numpy as np
from itertools import combinations

def read_input_file(file_path):
    """Reads the input from the file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def conv(inp):
    return 0 if inp == "." else 1

def parse_input(lines):
    seqs = [list(map(conv, [*line])) for line in lines]
    return seqs


fp = "input"
f = read_input_file(fp)
mat = np.asarray(parse_input(f))

def get_ones_positions(matrix):
    """ Returns the positions of 1s in the matrix """
    return [(i, j) for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) if matrix[i, j] == 1]

pos = get_ones_positions(mat)

def adjusted_manhattan_distance(point1, point2, empty_rows, empty_cols):
    dx = abs(point1[0] - point2[0])
    dy = abs(point1[1] - point2[1])

    # Calculate the number of expanded rows and columns in the path
    expanded_rows = sum(1 for i in range(min(point1[0], point2[0]), max(point1[0], point2[0])) if i in empty_rows)
    expanded_cols = sum(1 for i in range(min(point1[1], point2[1]), max(point1[1], point2[1])) if i in empty_cols)

    # Adjust distance calculation
    return (dx - expanded_rows) + expanded_rows * 1000000 + (dy - expanded_cols) + expanded_cols * 1000000

# Find empty rows and columns
empty_rows = [i for i, row in enumerate(mat) if all(row == 0)]
empty_cols = [i for i, col in enumerate(mat.T) if all(col == 0)]

# Calculate adjusted distances
all_distances = [adjusted_manhattan_distance(start, end, empty_rows, empty_cols) for start, end in combinations(pos, 2)]

# Sum of all distances
total_distance = sum(all_distances)
print("Total distance:", total_distance)

