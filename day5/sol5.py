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

def find_lowest_location(input_str):
    seeds, mappings = parse_input(input_str)
    final_locations = []

    for seed in seeds:
        current_number = seed
        for category in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
            current_number = map_number(current_number, mappings[category])
        final_locations.append(current_number)

    return min(final_locations)

input_str = read_input_file("sample")

# Call the function with the provided input
lowest_location = find_lowest_location(input_str)
print(lowest_location)
