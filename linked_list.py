# Nodes and Linked Lists

class Node:
    # An object for storing a single node of a linked list.
    # Models two attributes - data and the link to the next node in the list
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
    
    # function provides more readable node info
    def __repr__(self):
        return "<Node data: %s>" % self.data

# Check that Node works
#N1 = Node(10)
#N2 = Node(20)
#N1.next_node = N2
#print(N1.next_node)


class LinkedList:
    # Singly linked list
    def __init__(self):
        self.head = None
        
    # function checks that list is empty
    def is_empty(self):
        return self.head == None
    
    # function returns the number of nodes in the list
    # takess O(n) time
    def size(self):
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
        
        return count
    
    # function adds new node containing data at the head of the list
    # takes O(1) time
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    # function returns a string representation of the list
    # takes O(n) time
    def __repr__(self):
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tai: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return '-> '.join(nodes)


# check that LinkedList works
l = LinkedList()
#N1 = Node(10)
#l.head = N1
l.add(1)
l.add(2)
l.add(3)
#print(l.size()) 
print(l)

# the above print(l) shows that when appending list, data is added to the end moving the previously stored data over to next node