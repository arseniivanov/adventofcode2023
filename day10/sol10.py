import numpy as np

def read_input_file(file_path):
    """Reads the input from the file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def parse_input(lines):
    seqs = [[*line] for line in lines]
    return seqs

def find_index_of_s(list_of_lists):
    for x, sublist in enumerate(list_of_lists):
        for y, char in enumerate(sublist):
            if char == 'S':
                return (x, y)
    return None  # Return None if 'S' is not found

fp = "input"
f = read_input_file(fp)
mat = np.asarray(parse_input(f))

move_map = {
    ('|', (1, 0)): (1, 0),   # Moving down, continue down
    ('|', (-1, 0)): (-1, 0), # Moving up, continue up
    ('-', (0, 1)): (0, 1),   # Moving right, continue right
    ('-', (0, -1)): (0, -1), # Moving left, continue left
    ('L', (1, 0)): (0, 1),  # Moving down, turn right
    ('L', (0, -1)): (-1, 0),  # Moving left, turn up
    ('J', (1, 0)): (0, -1), # Moving down, turn left
    ('J', (0, 1)): (-1, 0),   # Moving right, turn up
    ('7', (-1, 0)): (0, -1),  # Moving up, turn left
    ('7', (0, 1)): (1, 0),  # Moving right, turn down
    ('F', (-1, 0)): (0, 1),   # Moving up, turn right
    ('F', (0, -1)): (1, 0), # Moving left, turn down
}

start_idx = find_index_of_s(mat)

#Hack to get the first move right, can be replaced by rule checker around S
if start_idx[1] > 10: 
    mv = (0, -1) #sample
else:
    mv = (0, 1) #input

cnt = 1
idx = (start_idx[0] + mv[0], start_idx[1] + mv[1])

visited_idxs = [start_idx, idx]

while idx != start_idx:
    mv = move_map[(mat[idx], mv)]
    idx = (idx[0] + mv[0], idx[1] + mv[1])
    visited_idxs.append(idx)
    #print("Moving with {} to idx {} which end up on {}".format(mv, idx, mat[idx]))
    cnt += 1

print("Furthermost tile: ", cnt//2)

#Part 2

from skimage.segmentation import flood_fill

def blow_up_maze(maze):
    WIDTH = 3
    HEIGHT = len(maze) * WIDTH
    WIDTH_EXPANDED = len(maze[0]) * WIDTH

    # Create an empty blown-up maze filled with zeros
    blown_up_maze = np.zeros((HEIGHT, WIDTH_EXPANDED), dtype=int)

    # Convert cell_maps to numpy arrays for easy assignment
    cell_maps = {
        "-": np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]),
        "|": np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]),
        "L": np.array([[0, 1, 0], [0, 1, 1], [0, 0, 0]]),
        "J": np.array([[0, 1, 0], [1, 1, 0], [0, 0, 0]]),
        "7": np.array([[0, 0, 0], [1, 1, 0], [0, 1, 0]]),
        "F": np.array([[0, 0, 0], [0, 1, 1], [0, 1, 0]]),
        "S": np.array([[0, 1, 0], [1, 1, 0], [0, 0, 0]]), #TODO Adjust to fit your input
        "0": np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    }

    # Populate the blown-up maze
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            blown_up_maze[i*WIDTH:(i+1)*WIDTH, j*WIDTH:(j+1)*WIDTH] = cell_maps[cell]

    return blown_up_maze

def count_enclosed_areas(expanded_mat):
    answer = 0
    rows, cols = expanded_mat.shape
    for row in range(rows - 2):  # Adjust range to avoid index out of bounds
        for col in range(cols - 2):
            if np.all(expanded_mat[row:row+3, col:col+3] == 0):  # Check 3x3 block of zeros
                answer += 1
                expanded_mat[row:row+3, col:col+3] = 2  # Mark the block to avoid recounting
    return answer

mat2 = np.zeros(mat.shape, dtype=int)
for i in visited_idxs:
    mat2[i] = 1

mat[mat2 != 1] = "0"

mat = np.asarray(blow_up_maze(mat))
mat = flood_fill(mat, (0,0), 1)

# Assuming expanded_mat is your flood-filled expanded maze
enclosed_area_count = count_enclosed_areas(mat)
print("Enclosed area count:", enclosed_area_count)

