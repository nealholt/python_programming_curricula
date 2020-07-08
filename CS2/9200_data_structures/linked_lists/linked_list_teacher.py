'''Alternatively, students could write tests and debug
my, intentionally broken linked list code.

Maybe students can write one function at a time with
lots of test cases specifically designed for the
function of the day.

stacks queues binary trees linked lists
These data structures could be acted out!

move on to stacks, queues, and binary trees.
https://medium.com/@gianpaul.r/applications-of-stacks-and-queues-f88fa33278d4

Stack application: reversing a sentence:
https://www.quora.com/What-are-some-sentences-that-if-read-backwards-have-a-new-meaning
https://www.dcode.fr/semordnilap-generator

Queue application: Call Center phone systems uses
Queues to hold people calling them in an order, until
a service representative is free.

linked list could be paired programming activity.
'''



'''
Source: https://www.interviewbit.com/courses/programming/topics/linked-lists/

This is also a massive resource:
https://www.geeksforgeeks.org/data-structures/linked-list/
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

    def removeHead(self):
        '''Remove the first item in the list without
        deleting the whole list. If there is nothing
        in the list, then do nothing.'''
        if self.head != None:
            self.head = self.head.next

    def removeTail(self):
        if self.head==None:
            return
        if self.head.next==None:
            self.head = None
            return
        n = self.head
        while n.next.next!=None:
            n = n.next
        n.next = None

    def addToTail(self, value):
        if self.head == None:
            self.addToHead(value)
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = Link(value)

    def addAtIndex(self, value, index):
        if self.head==None:
            self.head = Link(value)
        else:
            i = 0
            temp=self.head
            while i+1<index:
                i+=1
                temp = temp.next
            n = Link(value)
            n.next = temp.next
            temp.next = n

    def removeIndex(self, i):
        if i == 0 and self.head != None:
            self.head = self.head.next
            return
        index = 1
        n = self.head
        while index < i and n.next!=None:
            n = n.next
            index += 1
        if n.next != None:
            n.next = n.next.next

    def removeValue(self, value):
        if self.head == None:
            return
        if self.head.val == value:
            self.head = self.head.next
            return
        n = self.head
        while n.next != None and n.next.val != value:
            n = n.next
        if n.next != None:
            n.next = n.next.next

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
        print(string[:len(string)-2])


linkl = LinkedList()
sentence = ['A','merry','little','surge','of','electricity','piped','by','automatic','alarm','from','the','mood','organ','beside','his','bed','awakened','Rick','Deckard']
for word in sentence:
    linkl.addToTail(word)
linkl.print()
print(linkl.getLength())
linkl.removeValue('little')
linkl.print()
linkl.removeIndex(7)
linkl.print()
linkl.removeIndex(0)
linkl.addToHead('The')
linkl.print()
