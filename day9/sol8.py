from functools import reduce

def read_input_file(file_path):
    """Reads the input from the file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def parse_input(lines, forward):
    # Splitting the input string into lines
    seqs = [list(map(int, line.strip().split()))[::forward] for line in lines]
    return seqs


fp = "input"
f = read_input_file(fp)

seqs = parse_input(f, -1)

tot_sum = 0
for seq in seqs:
    facs = [seq[-1]]
    while not all([s == 0 for s in seq]):
        seq = [seq[x+1]-seq[x] for x in range(len(seq)-1)]
        facs.append(seq[-1])
    tot_sum += sum(facs)

print(tot_sum)
