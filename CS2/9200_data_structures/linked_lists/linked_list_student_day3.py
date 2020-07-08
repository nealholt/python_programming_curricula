'''
Fill in the code to make the addAtIndex function work
in the linked list class below.

You can and should use previous code that you wrote if
it is useful.
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

    def addAtIndex(self, value, index):
        '''Add the value at the index given.

        Example: Suppose we want to add the value A at
        index 1 and the list is currently Q->W->E->None
        Then the list should become
        Q->A->W->E->None

        If index is 0 then you want to add to the head.
        If index is the same as length then you want
        to add to the tail.

        But what if the index is inbetween?
        You will have to go through the list one Link
        at a time. Read the getLength function carefully.
        It will help you figure out what to do.

        This function does not return anything.
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
linkl.addAtIndex('A',0)

print('The list should contain only A:')
linkl.print()
#Verify that the add worked correctly.
points = 0
try:
    if linkl.getLength() == 1:
        points += 1
    if linkl.head!=None and linkl.head.val == 'A':
        points += 1
    if linkl.head!=None and linkl.head.next == None:
        points += 1
except:
    pass

linkl.addAtIndex('B',1)
linkl.addAtIndex('C',1)
linkl.addAtIndex('D',2)

print('The list should contain A, C, D, B:')
linkl.print()
try:
    #Verify that the add worked correctly.
    if linkl.getLength() == 4:
        points += 1
        print('a')
    if linkl.head!=None and linkl.head.next!=None and linkl.head.next.val == 'C':
        points += 1
        print('b')
    if linkl.head!=None and linkl.head.next!=None and linkl.head.next.next!=None and linkl.head.next.next.val == 'D':
        points += 1
        print('c')
    if linkl.head!=None and linkl.head.next!=None and linkl.head.next.next!=None and linkl.head.next.next.next != None:
        points += 1
        print('d')
except:
    pass

try:
    if linkl.head.val == 'A':
        points += 1
        print('e')
except:
    pass
try:
    if linkl.head.next.val == 'C':
        points += 1
        print('f')
except:
    pass
try:
    if linkl.head.next.next.val == 'D':
        points += 1
        print('g')
except:
    pass
try:
    if linkl.head.next.next.next.val == 'B':
        points += 1
        print('h')
except:
    pass
try:
    if linkl.head.next.next.next.next == None:
        points += 1
        print('i')
except:
    pass

print('Your code scored '+str(points)+' out of 12')
