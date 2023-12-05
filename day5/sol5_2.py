def read_input_file(file_path):
    """Reads the input from the file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def parse_input(input_str):
    # Splitting the input string into lines
    lines = input_str.split('\n')

    # Parsing seeds
    seeds = list(map(int, lines[0].split(':')[1].strip().split()))

    # Parsing mappings
    mappings = {}
    current_map = None
    for line in lines[1:]:
        if 'map:' in line:
            current_map = line.split(' map:')[0].strip()
            mappings[current_map] = []
        else:
            parts = list(map(int, line.split()))
            if parts:
                mappings[current_map].append(parts)

    return seeds, mappings

def map_number(number, mapping):
    # Check each range in the mapping
    for dest_start, src_start, length in mapping:
        if src_start <= number < src_start + length:
            # Calculate the offset from the start of the source range
            offset = number - src_start
            # Map the number to the destination range
            return dest_start + offset
    # If the number is not in any range, it maps to itself
    return number

def parse_elements_in_pairs(lst):
    """ Parses elements from the list in pairs. """
    return [lst[i:i + 2] for i in range(0, len(lst), 2)]

def find_lowest_location(input_str):
    seeds, mappings = parse_input(input_str)
    final_locations = []
    pairs = parse_elements_in_pairs(seeds)

    step = 100000
    small_step = 10000
    smaller_step = 100
    decreased = True

    pairs = [pairs[4]]

    for d, pair in enumerate(pairs):
        c = pair[0]
        while c <= pair[0] + pair[1]:
            for category in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
                current_number = map_number(c, mappings[category])
                if current_number <= 497:
                    final_locations.append(current_number)
                    print(final_locations)
                if current_number == 497:
                    if decreased:
                        c -= small_step
                        print(c)
                        exit()
                    decreased = False
                    small_step = 1
            c += small_step
        if not decreased:
            break

    return min(final_locations)

input_str = read_input_file("input")

# Call the function with the provided input
lowest_location = find_lowest_location(input_str)
print(lowest_location)
