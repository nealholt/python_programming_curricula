'''
Fill in the code to make the addToHead function work
in the linked list class below.

Here is an example of how to create a new Link containing
the value 3:
    n = Link(3)
Here is an example of how to create a new Link containing
the value of the variable v:
    n = Link(v)
'''

# Link class
class Link:
    # Function to initialize the node object
    def __init__(self, v):
        self.val = v  # Assign value
        self.next = None  # Initialize next as null

# Linked List class
class LinkedList:
    # Function to initialize the Linked List
    def __init__(self):
        self.head = None

    def getLength(self):
        length = 0
        n = self.head
        while n!=None:
            length += 1
            n = n.next
        return length

    def print(self):
        n = self.head
        string = ''
        while n!=None:
            string += str(n.val)+', '
            n = n.next
        #Print after chopping off the final comma and space
        print(string[:len(string)-2])

    def addToHead(self, value):
        '''Add the value at the head of the list.

        Suppose we want to add the value A.

        If the list is None
        then the list becomes A->None

        If the list is something like B->C->None
        then the list becomes A->B->C->None

        This function does not return anything.
        '''
        pass #TODO: Write code here.


#Create a linked list.
linkl = LinkedList()
#Add C to the list.
linkl.addToHead('C')
#Print the list.
print('The list should contain only C:')
linkl.print()
#Verify that the add worked correctly.
points = 0
if linkl.getLength() == 1:
    points += 1
if linkl.head!=None and linkl.head.val == 'C':
    points += 1
if linkl.head!=None and linkl.head.next == None:
    points += 1
#Add B and A to the list.
linkl.addToHead('B')
linkl.addToHead('A')
#Print the list.
print('The list should contain A,B,C:')
linkl.print()
#Verify that the add worked correctly.
if linkl.getLength() == 3:
    points += 1
if linkl.head!=None and linkl.head.val == 'A':
    points += 1
if linkl.head!=None and linkl.head.next != None:
    points += 1
if linkl.head!=None and linkl.head.next!=None and linkl.head.next.val == 'B':
    points += 1
if linkl.head!=None and linkl.head.next!=None and linkl.head.next.next != None:
    points += 1
if linkl.head!=None and linkl.head.next!=None and linkl.head.next.next!=None and linkl.head.next.next.val == 'C':
    points += 1
if linkl.head!=None and linkl.head.next!=None and linkl.head.next.next!=None and linkl.head.next.next.next == None:
    points += 1

print('Your code scored '+str(points)+' out of 10')



