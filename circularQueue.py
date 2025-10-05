 
class circularQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*size
        self.front = self.rear = -1
    
    def enque(self, element):
        if (self.rear + 1) % self.size == self.front:
            print("queue is full")
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = element
    
    def deque(self):
        if self.front == -1:
            print('underflow')
            return
        else:
            element = self.arr[self.front]
            print('dequed', element)
            self.arr[self.front] = None
            if self.front == self.rear: self.front = self.rear = -1
            else: self.front = (self.front + 1) % self.size
            return element

    
    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        i = self.front
        while True:
            print(self.arr[i], end=' ')
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


if '__main__':
    a = circularQueue(5)
    a.enque(1)
    a.enque(2)
    a.enque(3)
    a.enque(4)
    a.enque(5)
    for x in range(4):
        num = a.deque()
        a.enque(num)
        a.display()