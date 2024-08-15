# Implement bogo-sorting method

import random
import sys
from load import load_numbers

nums = load_numbers(sys.argv[1])

# Function that determines if list of numbers is sorted or not, return boolean
def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

# Function to implement bogo sorting on list of numbers
def bogo_sort(values):
    # set variable to track number of sorting attempts
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values

print(bogo_sort(nums))