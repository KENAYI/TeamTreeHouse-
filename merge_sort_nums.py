# Merge sort more efficient than 

import sys
from load import load_numbers

nums = load_numbers(sys.argv[1])

def merge_sort(values):
    # stopping condition
    if len(values) <= 1:
        return values
    # find middle number by finding its index
    middle_index = len(values) // 2
    # split list of values into two, L R
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    # print statement shows function working bts
    #print("%15s %-15s" %(left_values, right_values))
    sorted_values = []
    
    left_index = 0
    right_index = 0
    
    while left_index < len(left_values) and right_index  < len(right_values):
        # look to copy over lowest values first
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    # one list L or R has an empty list, while the other contains one value thus
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values

sorted_numbers = merge_sort(nums)
print(sorted_numbers)