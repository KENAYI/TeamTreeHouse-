# Linear search

def linear_search(list, target):
#Returns the index position  of the target if found, else returns None

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

# Write linear search that accepts and index value and prints its position, unless not found

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list!")
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)