def from_hex(val):
    out = val[2:-1]
    return int(out[-1]), int(out[:-1], 16)

def conv(row):
    row = row.split(" ")
    return row[0], int(row[1]), from_hex(row[2])

def read_data():
    with open("input") as f:
        return [tuple(conv(row)) for row in f.read().splitlines()]

def gauss_area(polygon):
    A = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i-1]
        x2, y2 = polygon[i]
        A += (x1 + x2) * (y2 - y1)
    return abs(A/2)

def boundary(polygon):
    cnt = 0
    for i in range(len(polygon)):
        dx = polygon[i][0] - polygon[i-1][0]
        dy = polygon[i][1] - polygon[i-1][1]
        cnt += max([abs(dx), abs(dy)])
    return cnt

def dual_solve(grid, DIRS, pt):
    path = [(0, 0)]
    x, y = 0, 0
    for ln in grid:
        if pt == 1:
            D, l, _ = ln
        else:
            _, _, (D, l) = ln
        dx, dy = DIRS[D]
        x, y = x + l*dx, y + l*dy
        path.append((x, y))

    A = gauss_area(path)
    B = boundary(path)
    filled = round(A - B/2 + 1)
    print(B + filled)

DIRS = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
    'R': (0, 1),
    'U': (1, 0),
    'L': (0, -1),
    'D': (-1, 0),
}

grid = read_data()

dual_solve(grid, DIRS, 2)
