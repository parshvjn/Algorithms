
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtHead(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtTail(self, data):
        new_node = node(data)
        if self.head == []:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def deleteAtHead(self):
        if self.head == []:
            return
        self.head = self.head.next
    
    def deleteAtTail(self):
        if self.head == []:
            return
        if self.head.next == None:
            self.head = []
            return
        
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
    
    def traversal(self): # ! not sure if was supposed to use this in other methods
        current = self.head
        while current: # while not null
            print(current.data)
            current = current.next

if '__main__':
    print('Initial Insertions')
    sll = SinglyLinkedList()
    sll.insertAtHead(1)
    sll.insertAtHead(2)
    sll.insertAtTail(3)
    sll.traversal()
    print("Deleted Head:")
    sll.deleteAtHead()
    sll.traversal()
    print("Deleted tail:")
    sll.deleteAtTail()
    sll.traversal()