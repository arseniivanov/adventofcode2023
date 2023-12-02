def read_all_lines(filename):
    """Read all lines from a file and return them as a list."""
    with open(filename, 'r') as file:
        return file.readlines()

def yield_lines(filename):
    """Lazily serve lines from a file upon demand."""
    with open(filename, 'r') as file:
        for line in file:
            yield line
