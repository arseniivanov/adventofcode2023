def read_data():
    with open("input") as f:
        return sum([calculate_hash(puz) for puz in f.read().strip().split(",")])

from collections import defaultdict, OrderedDict
import re

def add_to_d(puz, d):
    lab, focal = re.split('[-=]', puz)
    hsh = calculate_hash(lab)
    if "-" in puz:
        if lab in d[hsh].keys():
            del d[hsh][lab]
    else:
        focal = int(focal)
        d[hsh][lab] = focal

def calcsum(d):
    totsum = 0
    for (k, v) in d.items():
        for c, lens in enumerate(v, 1):
            totsum += (k+1)*c * v[lens]
    return totsum

def read_data_2():
    with open("input") as f:
        d = defaultdict(OrderedDict)
        for puz in f.read().strip().split(","):
            add_to_d(puz, d)
        print(d)
    return calcsum(d)

def calculate_hash(input_string):
    current_value = 0
    for char in input_string:
        # Determine the ASCII code
        ascii_code = ord(char)
        # Increase the current value by ASCII code
        current_value += ascii_code
        # Multiply by 17
        current_value *= 17
        # Remainder of division by 256
        current_value %= 256

    return current_value

h = read_data_2()
print(h)
