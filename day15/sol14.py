import numpy as np

def cmap(c):
    if c == "O":
        return 1
    elif c == "#":
        return 2
    else:
        return 0

def read_data():
    with open("sample") as f:
        return [list(map(cmap,puz)) for puz in f.read().splitlines()]

def move_ones_to_left(matrix):
    nrows, ncols = matrix.shape
    for row in range(nrows):
        for col in range(1, ncols):
            # Check if the current element is 1
            if matrix[row, col] == 1:
                current_col = col
                # Move the 1 to the left as far as possible
                while current_col > 0 and matrix[row, current_col - 1] == 0:
                    # Swap the 1 and the 0
                    matrix[row, current_col], matrix[row, current_col - 1] = matrix[row, current_col - 1], matrix[row, current_col]
                    current_col -= 1
    return matrix

h = np.asarray(read_data()).T

last_4_cache = [np.zeros(h.shape)]*4
c_counter = 0

num = 1000000000*4

di = ["N", "W", "S", "E"]
for i in range(num):
    h = move_ones_to_left(h)
    idx = i%4
    if np.array_equal(last_4_cache[idx], h):
        c_counter += 1
    else:
        c_counter = 0

    if c_counter == 4:
        print(di[idx])
        #Cycle detected, we are in theory on roll num-(i%4) finish the cycle (roll E)
        num_rolls_left = (num-i)%4
        print(num_rolls_left)
        print(h)
        for i in range(num_rolls_left):
            h = np.rot90(h, axes=(1, 0))
            #h = move_ones_to_left(h)
        h = h.T
        print(h)
        print(i)
        break
    last_4_cache[idx] = h
    h = np.rot90(h, axes=(1, 0))

totsum = 0
for c, row in enumerate(np.flip(h, 0), 1):
    totsum += sum(row == 1)*c

print(totsum)

