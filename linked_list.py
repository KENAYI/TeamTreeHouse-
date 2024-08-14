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
    # takes O(n) time
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
    
    # Search for the first node containing data that matches the key
    # Takes O(n) as it has to run through is value looking for key, linear time
    def search(self, key):
        current = self.head
        
        # check that current data matches key
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
            # if current doesn't contain value of key, return None
        return None
    
    # Inserts a new node containing data at index position
    # Insertion takes O(1) but finding the node at the insertion point takes O(n) time
    # Thus, overall it takes O(n) time
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = Node.next_node
                position -= 1
            
            # prev is node before inserted node and next is node after it    
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node
    
    # Removes Node containing data that matches the key
    # Takes O(n) time
    def remove(self, key):
        current = self.head
        prev = None
        # stopping condition for loop
        found = False
        
        while current and not found:
            if current.data == key and current == self.head:
                found = True
                # since first node is now removed, reference head node to the subsequent node
                self.head = current.next_node
            elif current.data == key:
                found = True
                # since the prev subsequent node contained key, reference head to subsequent node as before
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node
            # returns node or None if key doesn't exist
            return current
    
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
print(l.search(2))
print(l)
# the above print(l) shows that when appending list, data is added to the end moving the previously stored data over to next node