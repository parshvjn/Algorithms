
class simpleQueue:
    def __init__(self, maxSize):
        self.arr = [None]*maxSize
        self.front = self.rear = -1
        self.maxSize = maxSize
    
    def overflow(self):
            return True if self.rear == self.maxSize - 1 else False
    
    def underflow(self):
        return True if self.front == -1 or self.front > self.rear else False

    def enque(self, value):
        if self.overflow():
            print('queue is full')
        else:
            if self.underflow():
                self.front = self.rear = 0
            else:
                self.rear += 1
            self.arr[self.rear] = value
    
    def deque(self):
        if self.underflow():
            print('array is empty')
        else:
            element = self.arr[self.front]
            print('elemnt:', element)
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
    
    def display(self):
        print(self.arr[self.front:self.rear+1])


if '__main__':
    a = simpleQueue(5)
    a.enque(2)
    a.enque(4.2)
    a.enque(7)
    a.enque(71)
    a.enque(72)
    a.display()
    a.deque()
    a.display()
    a.enque(100)