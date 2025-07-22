
class node:
    def __init__(self, data):
        self.data = data
        self.next = None # holds address of the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None # address of entire list
    
    def insertAtHead(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        print('insert: ', data)
    
    def insertAtTail(self, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            print('insert: ', data)
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print('insert: ', data)
    
    def deleteAtHead(self):
        if self.head == []:
            return
        print('deleted:', self.head.data)
        self.head = self.head.next
    
    def deleteAtTail(self):
        if self.head == []:
            return
        if self.head.next == None:
            print('deleted:', self.head.data)
            self.head = []
            return
        
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        print('deleted:', second_last.next.data)
        second_last.next = None
    
    def traversal(self): # ! not sure if was supposed to use this in other methods
        current = self.head
        while current: # while not null
            print(current.data)
            current = current.next
    
    def peak(self): # return the last element or top on a stack
        if self.head == None:
            print('List is empty')
            return None

        last = self.head
        while last.next:
            last = last.next
        print(last.data)

if '__main__':
    # Stack with Singly Linked List
    # sll = SinglyLinkedList()
    # sll.insertAtTail(1)
    # sll.insertAtTail(2)
    # sll.insertAtTail(3)
    # # sll.traversal()
    # sll.peak()

    # sll.deleteAtTail()
    # sll.peak()
    # sll.deleteAtTail()
    # sll.deleteAtTail()

    # Simple Queue with Singly Linked List
    ssl = SinglyLinkedList()
    ssl.insertAtTail(1)
    ssl.insertAtTail(2)
    ssl.insertAtTail(3)
    ssl.deleteAtHead()
    ssl.deleteAtHead()
    ssl.deleteAtHead()