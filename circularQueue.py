
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
    a.enque(20)
    a.enque(23)
    a.enque(240)
    a.enque(23)
    a.enque(23)
    a.deque()
    a.deque()
    # print(a.rear)
    a.enque(230)
    a.enque(240)
    a.enque(240)
    # a.deque()
    a.display()