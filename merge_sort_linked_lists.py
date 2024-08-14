# Merge and Sort Linked Lists

from linked_list import LinkedList

# Sorts a linked list in ascending order
# - Recursively divide the linked list into sub-lists containing a single node
# - Repeatedly merge the sub-lists to produce sorted sub-lists until one remains
# Returns a sorted linked list

# Takes O(n log n) time
# Takes O(n) space
def merge_sort(linked_list):
    # if linked list contains just 1 or no elements return linked list, stopping condition
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

# Divide the unsorted linked list at midpoint into sub-lists
# Takes O(log n) time
def split(linked_list):
    # if linked list is empty or containing just one element, assign to left half leaving right half empty
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        
        return left_half, right_half
    else:
        # for none empty linked lists
        size = linked_list.size()
        midp = size//2
    
        # use node_at_index with midp to get the node at the midpoint of the linked list
        midp_node = linked_list.node_at_index(midp-1) # implement -1 because size is 1 > index

        left_half = linked_list
        right_half = LinkedList()
        # assign next node after midpoint as start of new right_half list
        right_half.head = midp_node.next_node
        # node at midpoint incidentally becomes tail node of new left_half list
        midp_node.next_node = None
    
        return left_half, right_half

# Merges two linked lists, sorting by data in node
# Returns a new merged list
# Takes O(n) time
# Runs in O(n) time
def merge(left, right):
    # create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    
    # add a fake head to be discarded later on
    merged.add(0)
    
    # sort current to the head of the linked list
    current = merged.head
    
    # obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head  
    
    # iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # if the head node of left is none, we're past the tail
        # add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to False
            right_head = right_head.next_node
        # if the head node of right is None, we're past the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
        # not at either tail node
        # obtain more data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on left < right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node
            # if data on left > right, set current to right node
            else:
                current.next_node = right_head
                # move right head to next node
                right_head = right_head.next_node
        # move current to next node
        current = current.next_node
    
    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    
    return merged

#l = LinkedList()
#l.add(10)
#l.add(2)
#l.add(44)
#l.add(15)
#l.add(200)

#print(l)
#sorted_linked_list = merge_sort(l)
#print(sorted_linked_list)