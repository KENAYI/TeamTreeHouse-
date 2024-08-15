# You call any of these functions with the path to a file you want to load.
# It loads the file contents, converts each line from a string to
# an integer, and returns them all as a Python list.
# Also converts strings in a list to strings in Python.

def load_numbers(file_name):
    nums = []
    with open(file_name) as f:
        for line in f:
            nums.append(int(line))
    return nums

def load_strings(file_name):
    strings = []
    with open(file_name) as f:
        for line in f:
            strings.append(line.rstrip())
    return strings