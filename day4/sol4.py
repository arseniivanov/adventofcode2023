def read_schematic(filename):
    with open(filename, 'r') as file:
        return [line.strip().split(": ")[-1].split(" | ") for line in file.readlines()]

inp = read_schematic("input")
summed = 0
for i in inp:
    cards, ans = i
    cards = set(map(int, cards.split()))
    ans = set(map(int, ans.split()))
    num = len(cards & ans)
    num = num if num == 0 or num == 1 else 2**(num-1)
    summed += num

print(summed)
