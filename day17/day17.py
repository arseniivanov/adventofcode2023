from heapq import heappush, heappop
import numpy as np

def read_data():
    with open("input") as f:
        return np.asarray([list(map(int,puz)) for puz in f.read().splitlines()])

def minimal_heat(start, end, mn, mx, grid):
    queue = [(0, *start, 0,0)]
    seen = set()
    while queue:
        heat,x,y,px,py = heappop(queue)
        if (x,y) == end:
            return heat
        if (x,y, px,py) in seen:
            continue
        seen.add((x,y, px,py))
        #After a step, we can only go to sides (forward option is different queue entry)
        for dx,dy in {(1,0),(0,1),(-1,0),(0,-1)} - {(px,py),(-px,-py)}:
            a,b,h = x,y,heat
            for i in range(1,mx+1):
                a,b=a+dx,b+dy
                if a < len(grid[0]) and b < len(grid) and a >= 0 and b >= 0:
                    h += grid[b][a]
                    if i>=mn:
                        heappush(queue, (h, a,b, dx,dy))

grid = read_data()
#print(minimal_heat((0,0),(len(grid)-1, len(grid[0])-1), 1, 3, grid))
print(minimal_heat((0,0),(len(grid)-1, len(grid[0])-1), 4, 10, grid))
