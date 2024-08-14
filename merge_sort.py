# Merge and Sort algorithms

# Sorts a list in ascending order
# Returns a new sorted list

# Divide - Find the midpoint of the list and divide into sub-lists
# Conquer = Recursive sort the sub-lists created in previous step
# Combine - merge the sorted sub-lists created in previous step

# Takes overall O(kn log n) time
def merge_sort(list):
    # returns list if only contains one element, stopping condition
    if len(list) <= 1:
        return list
    
    # divide
    left_half, right_half = split(list)
    
    # conquer, recursive
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

# Divide the unsorted list at midpoint into sub-lists
# Returns two sub-lists, left and right 
# Takes overall O(k log n) time, as : slice takes O(k) runtime
def split(list):
    # determine midpoint for list, using floor operator
    midp = len(list)//2
    left = list[:midp]
    right = list[midp:]
    
    return left, right

# Merges two lists sorting them in the process
# Returns new merged list
# Takes overall O(n) time
def merge(left, right):
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
        # if left[i] >= right[j]
            l.append(right[j])
            j += 1
    
    # where right list is shorter than left
    while i < len(left):
        l.append(left[i])
        i += 1
    
    # where left list is shorter than right
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)
    
    # simply returns list if only contains one or less element, stopping condition
    if n == 0 or n == 1:
        return True
    
    # this recursive condition verifies that each first element [0] is < the second [1]
    # it does this for each sublist until sublist contains just 1 element, thus calling on stopping condition above
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [78, 49, 1, 30, 52, 9, 25]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l)) 