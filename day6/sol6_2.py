def read_input_file(file_path):
    """Reads the input from the file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def parse_input(input_str):
    # Splitting the input string into lines
    lines = input_str.split('\n')
    times = list(map(int, [lines[0].split(':')[1].replace(" ", "")]))
    distances = list(map(int, [lines[1].split(':')[1].replace(" ", "")]))
    return zip(times, distances)

f = read_input_file("input")
data = parse_input(f)

#t^2 - t*t_max + (d + 1) = 0
#Find roots, take differ
import math

def roots(t, d):
    rt = math.sqrt(t**2 - 4*(d + 1))
    return (t - rt)/2, (t + rt)/2


cul = 1
for t_max, d in data:
    t1, t2 = roots(t_max, d)
    t1 = math.ceil(t1)
    t2 = math.floor(t2)
    cul *= len(range(t1, t2+1))

print(cul)

