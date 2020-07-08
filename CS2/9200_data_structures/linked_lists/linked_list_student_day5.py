'''
Fill in the code to make the removeValue function work
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

    def removeValue(self, value):
        '''Remove the first instance of value
        from the list.

        Example: Suppose we want to remove 'A' and the
        list is currently A->C->G->A->C->None
        Then the list should become
        C->G->A->C->None

        If we remove 'A' again the list should become
        C->G->C->None

        If the list is empty, do nothing.

        If the user asks to remove a value that is not in
        the list, do nothing.

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
linkl.addToHead('A')
linkl.addToHead('G')
linkl.addToHead('C')
linkl.addToHead('A')

points = 0
try:
    if linkl.getLength() == 5:
        points += 1
except:
    pass

linkl.removeValue('A')

try:
    if linkl.getLength() == 4:
        points += 1
        print('a')
    if linkl.head.val=='C':
        points += 1
        print('b')
    if linkl.head.next.val=='G':
        points += 1
        print('c')
    if linkl.head.next.next.val=='A':
        points += 1
        print('d')
except:
    pass

linkl.removeValue('A')

try:
    if linkl.getLength() == 3:
        points += 1
        print('e')
    if linkl.head.val=='C':
        points += 1
        print('f')
    if linkl.head.next.val=='G':
        points += 1
        print('g')
    if linkl.head.next.next.val=='C':
        points += 1
        print('h')
    if linkl.head.next.next.next==None:
        points += 1
        print('i')
except:
    pass

try:
    linkl.removeValue('A')
    print('j')
    points += 1
    if linkl.getLength() == 3:
        points += 1
        print('k')
except:
    pass

linkl.removeValue('G')

try:
    if linkl.getLength() == 2:
        points += 1
        print('l')
    if linkl.head.val=='C':
        points += 1
        print('m')
    if linkl.head.next.val=='C':
        points += 1
        print('n')
    if linkl.head.next.next==None:
        points += 1
        print('o')
except:
    pass

linkl.removeValue('C')
linkl.removeValue('C')

try:
    if linkl.getLength() == 0:
        points += 1
        print('p')
    if linkl.head==None:
        points += 1
        print('q')
except:
    pass

try:
    linkl.removeValue('C')
    points += 1
    print('r')
except:
    pass

print('Your code scored '+str(points)+' out of 19')
