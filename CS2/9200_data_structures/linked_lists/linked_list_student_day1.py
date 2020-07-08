'''
Fill in the code to make the addToTail function work
in the linked list class below.

You can check if head is None like this:
if self.head == None:

You can check if head's next is None like this:
if self.head.next == None:

If you try to check next when your current node is None,
you will get an error.
For example, this will cause an error:
self.head = None
print(self.head.next)
'''

# Linked list example in Python
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

    def addToTail(self, value):
        '''Add the value at the tail of the list.

        Suppose we want to add the value A.

        If the list is None
        then the list becomes A->None

        If the list is something like B->C->None
        then the list becomes B->C->A->None

        This function does not return anything.

        You may add other functions or modify other code to
        make this work, but you may not use lists.

        Hint: Read through getLength to understand how
        to find the end of the current list.
        '''
        pass #TODO: Write code here.


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


linkl = LinkedList()
linkl.addToTail('A')

print('The list should contain only A:')
linkl.print()
#Verify that the add worked correctly.
points = 0
if linkl.getLength() == 1:
    points += 1
if linkl.head!=None and linkl.head.val == 'A':
    points += 1
if linkl.head!=None and linkl.head.next == None:
    points += 1

linkl.addToTail('B')
linkl.addToTail('C')

print('The list should contain A, B, C:')
linkl.print()
#Verify that the add worked correctly.
if linkl.getLength() == 3:
    points += 1
if linkl.head!=None and linkl.head.next!=None and linkl.head.next.val == 'B':
    points += 1
if linkl.head!=None and linkl.head.next!=None and linkl.head.next.next!=None and linkl.head.next.next.val == 'C':
    points += 1
if linkl.head!=None and linkl.head.next!=None and linkl.head.next.next!=None and linkl.head.next.next.next == None:
    points += 1

print('Your code scored '+str(points)+' out of 7')
