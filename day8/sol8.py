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

cnt = 0
step = "AAA"

while step != "ZZZ":
    step = dct[step][ins_dct[ins[cnt%len(ins)]]]
    cnt += 1

print(cnt)

