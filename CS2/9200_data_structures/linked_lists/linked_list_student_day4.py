'''
Fill in the code to make the removeTail function work
in the linked list class below.

You can use any previous linked list code.
An addToHead function has been provided.
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

    def addToHead(self, value):
        temp = self.head
        self.head = Link(value)
        self.head.next = temp

    def removeTail(self):
        '''Remove the last item in the list.

        Example: If our list contains A->B->C->None
        and we call removeTail then we should have
        A->B->None

        If there is nothing in the list, this function
        should do nothing.

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
linkl.addToHead('C')
linkl.addToHead('B')
linkl.addToHead('A')

points = 0
try:
    if linkl.getLength() == 3:
        points += 1
except:
    pass

linkl.removeTail()

try:
    if linkl.getLength() == 2:
        points += 1
        print('a')
    if linkl.head.val=='A':
        points += 1
        print('b')
    if linkl.head.next.val=='B':
        points += 1
        print('c')
    if linkl.head.next.next==None:
        points += 1
        print('d')
except:
    pass

linkl.removeTail()

try:
    if linkl.getLength() == 1:
        points += 1
        print('e')
    if linkl.head.val=='A':
        points += 1
        print('f')
    if linkl.head.next==None:
        points += 1
        print('g')
except:
    pass

linkl.removeTail()

try:
    if linkl.getLength() == 0:
        points += 1
        print('h')
    if linkl.head==None:
        points += 1
        print('i')
except:
    pass

try:
    linkl.removeTail()
    if linkl.getLength() == 0:
        points += 1
        print('j')
    if linkl.head==None:
        points += 1
        print('k')
except:
    pass


print('Your code scored '+str(points)+' out of 12')
