from collections import defaultdict

def read_schematic(filename):
    with open(filename, 'r') as file:
        return [line.strip().split(": ")[-1].split(" | ") for line in file.readlines()]

def c_num(cards, ans):
    cards = set(map(int, cards.split()))
    ans = set(map(int, ans.split()))
    return len(cards & ans)

def pop_d(idx, num, d):
    for i in range(1,num+1):
        r = 1 if idx != 1 else 0
        d[idx+i] += (1*d[idx] + r)
    if idx != 1:
        d[idx] += 1

inp = read_schematic("input")
d = defaultdict(int)
d[1] = 1
c, a = inp[0]
pop_d(1, c_num(c, a), d)
for c, i in enumerate(inp[1:], 2):
    cards, ans = i
    num = c_num(cards, ans)
    pop_d(c, num, d)

print(sum(d.values()))

