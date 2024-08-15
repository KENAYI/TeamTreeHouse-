# Quicksort proves to be more efficient than bogo_sort and selection_sort

import sys
from load import load_numbers 

nums = load_numbers(sys.argv[1])

# Function implements quicksort using recursion 
def quicksort(values):
    # stopping function
    if len(values) <= 1:
        return values
    
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
        # print statement shows function working bts
        #print("%15s %ls %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

print(nums)
sorted_numbers = quicksort(nums)
print(sorted_numbers)