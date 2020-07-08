'''
Fill in the code to make the removeHead function work
in the linked list class below.
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

    def removeHead(self):
        '''Remove the first item in the list without
        deleting the whole list. If there is nothing
        in the list, then do nothing.'''
        pass #TODO: Write code here.


    def addToHead(self, value):
        temp = self.head
        self.head = Link(value)
        self.head.next = temp

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
linkl.addToHead('C')
linkl.addToHead('B')
linkl.addToHead('A')

linkl.removeHead()

#Verify that the add worked correctly.
points = 0
if linkl.getLength() == 2:
    points += 1
    print('a')

try:
    if linkl.head.val == 'B':
        points += 1
        print('b')
except:
    pass

try:
    if linkl.head.next.val == 'C':
        points += 1
        print('c')
except:
    pass

try:
    if linkl.head.next.next == None:
        points += 1
        print('d')
except:
    pass

linkl.removeHead()

#Verify that the add worked correctly.
if linkl.getLength() == 1:
    points += 1
    print('e')

try:
    if linkl.head.val == 'C':
        points += 1
        print('f')
except:
    pass

try:
    if linkl.head.next == None:
        points += 1
        print('g')
except:
    pass

linkl.removeHead()

#Verify that the add worked correctly.
if linkl.getLength() == 0:
    points += 1
    print('h')

try:
    if linkl.head == None:
        points += 1
        print('i')
except:
    pass

try:
    linkl.removeHead()
    linkl.removeHead()
    linkl.removeHead()
    points += 1
except:
    pass
print('Your code scored '+str(points)+' out of 10')
