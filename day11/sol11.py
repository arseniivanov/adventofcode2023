import numpy as np

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

rows = []
cols = []
for c, row in enumerate(mat):
    if all(row == 0):
        rows.append(c)
for c, row in enumerate(mat.T):
    if all(row == 0):
        cols.append(c)

# Insert new rows of 0s
for row_idx in reversed(rows):  # Use reversed to avoid offset issues when inserting
    mat = np.insert(mat, row_idx, 0, axis=0)

# Insert new columns of 0s
for col_idx in reversed(cols):  # Use reversed for the same reason
    mat = np.insert(mat, col_idx, 0, axis=1)

# mat now has additional rows and columns of 0s where needed
print(mat)

def get_ones_positions(matrix):
    """ Returns the positions of 1s in the matrix """
    return [(i, j) for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) if matrix[i, j] == 1]

pos = get_ones_positions(mat)

print(pos)

def manhattan_distance(point1, point2):
    """ Calculate Manhattan Distance between two points """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


from itertools import combinations
all_distances = [manhattan_distance(start, end) for start, end in combinations(pos, 2)]

print("Total number of paths:", len(all_distances))
print("All paths distances:", sum(all_distances))
