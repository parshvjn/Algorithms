class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class doublyLinkedList:
    def __init__(self):
        self.head = None

    def insertBeg(self, element):
        newNode = node(element)
        if self.head != None:
            newNode.right = self.head
            self.head.left = newNode
        self.head = newNode
    
    def insertEnd(self, element):
        newNode = node(element)
        if self.head == None:
            self.head = newNode
            return
        current = self.head
        while current.right:
            current = current.right
        current.right = newNode
        newNode.left = current
    
    def deleteBeg(self):
        if self.head == None:
            print("empty")
            return
        self.head = self.head.right
        if self.head:
            self.head.left = None
    
    def deleteEnd(self):
        if self.head == None:
            print("empty")
            return
        current = self.head
        while current.right:
            current = current.right
        if current.left:
            current.left.right = None
        else:
            self.head = None

    def traversalForward(self):
        current = self.head
        while current:
            print(current.data, end = " -> " if current.right else "")
            current = current.right
        print()
    
    def traversalBackward(self):
        current = self.head
        if not current:
            print("empty")
            return
        while current.right:
            current = current.right
        while current:
            print(current.data, end = " <- " if current.left else "")
            current = current.left
        print()

if '__main__':
    l = doublyLinkedList()
    l.insertBeg(2)
    l.insertBeg(1)
    l.insertBeg(4)
    l.insertBeg(5)
    l.insertEnd(3)
    l.traversalForward()
    l.traversalBackward()
    l.deleteBeg()
    l.deleteEnd()
    l.traversalForward()
    l.traversalBackward()