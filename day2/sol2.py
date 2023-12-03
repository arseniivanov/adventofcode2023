def read_all_lines(filename):
    """Read all lines from a file and return them as a list."""
    with open(filename, 'r') as file:
        return file.read().splitlines() 

s = 0
d = {"red": 12, "green": 13, "blue": 14}
for c, x in enumerate(read_all_lines("input"), 1):
    y = x.split(": ")[1]
    game = True
    for l in y.split("; "):
        for k in l.split(", "):
            k = k.split(" ")
            if d[k[1]] < int(k[0]):
                game = False
                break
    if game:
        s += c

print(s)


s = 0
for c, x in enumerate(read_all_lines("input"), 1):
    d = {"red": 0, "green": 0, "blue": 0}
    y = x.split(": ")[1]
    for l in y.split("; "):
        for k in l.split(", "):
            k = k.split(" ")
            if d[k[1]] < int(k[0]):
                d[k[1]] = int(k[0])
    product = 1
    for value in d.values():
        product *= value
    s += product
print(s)
