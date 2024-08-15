# Selection sort, which is more efficient than bogo sorting

import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# Function does selection sort
def selection_sort(values):
    sorted_list = []
    #print("%-25s %-25s" % (values, sorted_list))
    for i in range(0, len(values)):
        # find minimum value in list, return it's index 
        index_to_move = index_of_min(values)
        # pop operation on the list to remove minimum value and add to end of sorted_list
        sorted_list.append(values.pop(index_to_move))
        # visualize initial list of numbers and numbers being filed into sorted_list 
        #print("%-25s %-25s" % (values, sorted_list))
    return sorted_list

# Function that picks out minimum values
def index_of_min(values):
    # mark first value in list
    min_index = 0
    for i in range(1, len(values)):
    # check if current value is less than previous minimum value
        if values[i] < values[min_index]:
        # when loop comes across smaller value, replace previous minimum value
            min_index = i
    return min_index

print(selection_sort(numbers))