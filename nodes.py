# Reference https://www.tutorialspoint.com/python/python_nodes.htm

### Nodes are all about pointers 

## NODES - 
class Daynames: 
    def __init__(self, dataval = None):
        self.dataval = dataval  # value
        self.nextval = None  #the pointer

e1 = Daynames('Monday')
e2 = Daynames('Wednesday')
e3 = Daynames('Tuesday')
e4 = Daynames('Thursday')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

thisvalue = e1

# Traversing the Nodes
while thisvalue:
    print("node day: ", thisvalue.dataval)
    thisvalue = thisvalue.nextval
# Executes the above code.  But how do I add a new day?  Do I have to hard code it into another e# variable?
Daynames()


### LINKED LISTS
class Node: 
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
    
class Singly_Linked_Lists:
    def __init__(self):
        self.headval = None

    # adding method for demonstrating traversing
    def listprint(self):
        printval = self.headval
        # this is the traversal method
        while printval is not None:
            print(f"linked list day: {printval.dataval}")
            printval = printval.nextval
        print('\n----------------------------')

    # for demonstrating creating a new node and inserting at beginning of list
    def AtBeginning(self, newdata):
        new_node = Node(newdata)

        # update the new node's val to existing node
        new_node.nextval = self.headval
        self.headval = new_node
    
    # for demonstrating creating a new node and inserting at end of list
    def AtEnd(self, newdata):
        # create a new Node(newdata) with the given input data and store it in a variable
        new_node = Node(newdata)
        # check length of node linked list, if it is empty, assign the node to the head of list
        if self.headval is None:
            self.headval = new_node
            return 
        # find the head(start) of linked list and store it in a variable (i.e. laste)
        laste = self.headval
        # while there is a NEXT node beyond the head node...
        while (laste.nextval):
            # reassign the next node to laste variable...
            laste = laste.nextval
        # if there is NOT a next value in the linked list, assign the nextval node(end node, null node) to be the value of the newdata 
        laste.nextval = new_node

# Set up initial nodes
list1 = Singly_Linked_Lists()
list1.headval = Node('Monday')
d2 = Node('Tuesday')
d3 = Node('Wednesday')

# link first node to second node
list1.headval.nextval = d2

# link second node to third node
d2.nextval = d3

## Traversing a Linked List
# Singly linked lists can only be traversed in only FORWARD direction starting from the first data element. We simply print the value of the next data element by assgining the pointer of the next node to the current data element.

list1.listprint( )

## Insertion into a Linked List
# Inserting at the Beginning - when inserting at the beginning of a Linked List, you want to reassign the nextval pointer to the current headval and reassigning the headval pointer to the new node being inserted.
list1.AtBeginning('Sunday')

# print with new day added at beginning.
list1.listprint()

# Inserting at the END - This involves pointing the next pointer of the the current last node of the linked list to the new data node. So the current last node of the linked list becomes the second last data node and the new node becomes the last node of the linked list.
list1.AtEnd('Thursday')  # insert this between Wednesday and Friday when doing insertion between 2 nodes of list.
list1.AtEnd('Friday')
list1.AtEnd('Saturday')

# print with new day added at end.
list1.listprint()

