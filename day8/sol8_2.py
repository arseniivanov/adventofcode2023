import math

def read_input_file(file_path):
    """Reads the input from the file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def trans(d):
    return [item.strip() for item in d.strip("()").split(",")]

def parse_input(input_str):
    # Splitting the input string into lines
    lines = input_str.split('\n')
    ins = lines[0]
    dct = {s : trans(d) for line in lines[2:-1] for s,d in [line.split(" = ")]}
    return ins, dct


fp = "input"
f = read_input_file(fp)
ins, dct = parse_input(f)
ins_dct = {"L":0, "R":1}

steps = [k for k in dct.keys() if k[-1] == "A"]
s_cnts = []

for step in steps:
    s_cnt = 0
    while step[-1] != "Z":
        step = dct[step][ins_dct[ins[s_cnt%len(ins)]]]
        s_cnt += 1
    s_cnts.append(s_cnt)

print(math.lcm(*s_cnts))

