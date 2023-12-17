from itertools import starmap, chain
from functools import partial
from operator import add
import numpy as np

def convert(x):
    if x == ".":
        return 0
    if x == "/":
        return 1
    if x == "\\":
        return 2
    if x == "-":
        return 3
    if x == "|":
        return 4

def read_data():
    with open("input") as f:
        return np.asarray([list(map(convert,puz)) for puz in f.read().splitlines()])

class Vector(tuple):
    def __add__(self, other):
        return Vector(starmap(add, zip(self, other)))

def V(*args):
    return Vector(args)

def out_of_grid(step, grid):
    return step[0] >= len(grid[0]) or step[0] < 0 or step[1] >= len(grid) or step[1] < 0

def energize(grid, start):
    stack, seen = [start], {start}
    while len(stack) > 0:
        cur, d = stack.pop(0)
        for step in STEPS[grid[cur]][d]:
            new = cur + step
            if out_of_grid(new, grid) or (new, step) in seen:
                continue
            stack.append((new, step))
            seen.add((new, step))
    return len(set(loc for loc, _ in seen))

RIGHT, DOWN, LEFT, UP = V(0, 1), V(1, 0), V(0, -1), V(-1, 0)

STEPS = {
    0: {RIGHT: [RIGHT], LEFT: [LEFT], DOWN: [DOWN], UP: [UP]},
    1: {RIGHT: [UP], LEFT: [DOWN], DOWN: [LEFT], UP: [RIGHT]},
    2: {RIGHT: [DOWN], LEFT: [UP], DOWN: [RIGHT], UP: [LEFT]},
    3: {RIGHT: [RIGHT], LEFT: [LEFT], DOWN: [LEFT, RIGHT], UP: [LEFT, RIGHT]},
    4: {RIGHT: [UP, DOWN], LEFT: [UP, DOWN], DOWN: [DOWN], UP: [UP]}
}

grid = read_data()
#print(energize(grid, (V(0,0), RIGHT)))

rows = len(grid)
cols = len(grid[0])

starts = chain(
    [(V(0, c), DOWN) for c in range(cols)],
    [(V(rows - 1, c), UP) for c in range(cols)],
    [(V(r, 0), RIGHT) for r in range(rows)],
    [(V(r, cols - 1), LEFT) for r in range(rows)]
)

print(max([energize(grid, (x)) for x in starts]))


