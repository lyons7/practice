# Linked lists: each element is a node. Each node has a value and a pointer pointing to the next value.
# You make a class, a class is ... WHAT?
# This is example how you would create a class of objects in Python

# Linked lists are not a native structure in Python (can't use 'built-in' Python), so we have to MAKE IT FROM SCRATCH

# You may have done FUNCTIONS, but maybe not OBJECTS


# Linked List: imagine a chain link fence? Linked list is a list of things all connected to one another. W/ an array I have to allocate all of this space
# in memory all the way. Linked list can grow over time, nodes don't have to be stored all in the same place in memory!
# Array is a contiguous block of memory. Memory-inefficient to make an array. Linked List lets you build it up one piece at a time.
# It's like a junk drawer where you can just throw stuff where you have space.
# 'Piecemeal' array

class Car:
    def __init__(self, color): # Initialize stuff you absolutely need
        self.color = color
        self.plate = None
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
car1 = Car('blue')
car1.start()
car1.stop()

# a node has a value -- 'next' stores a location in memory, 'value' stores a value in that location
# a node has a pointer, initially pointing to nothing, then to the next node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    # To traverse this linked list:
    def traverse(self):
        node = self
        while node != None: # As long as there is a node, keep going
            print (node.value) # Print what is at that node
            node = node.next # Re-set your node to the next node in your linked list

# Compact way
node1 = Node(1) # Defining what is in node 1
node1.next = Node(2) # Defining what node 2 is
node1.next.next = Node(50) # Defining what node 3 is. Compact version is .next.next.next

# Less compact version
# node2 = Node(2) # Set value (but it is not yet linked to anything!)
# node1.next = node2 # Assign it to the next pointer (chaining this node to the list)
# Do this again...
# node3 = Node(50)
# node2.next = node3
print(node1.value)
print(node1.next.next.value)

# From this current node, go on to print all of the nodes linked to it
node1.traverse()
# node1.next.traverse()


# Ok new problem: Write code to delete a node. You need to specify the head node and the value of the node you want deleted.
# Add on to our Node class to build-in a capability to delete things.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def traverse(self):
        node = self
        while node != None:
            print (node.value)
            node = node.next
    # New aspect we are adding here -- delete a node.
    # To do make a connection between the previous node and the current node’s next node (basically deleting the current node),
    # it is important to keep track of the previous node
    def removeNode(self, value):
        node = self
        # Very difficult to delete head of singly linked list
        if node.value == value:
            # Do something? # Di
        else:
            while node.next != None:
                if node.next.value == value:
                    node.next = node.next.next
                else:
                    node = node.
# New linked list
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4

node1.deletenode(3)

node1.traverse()
