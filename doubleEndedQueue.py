class doubleEndedQueue:
    def __init__(self, size):
        self.size = size
        self.front = self.rear = -1 # ! I changed from None to -1, is it fine? -- methods were giving error for adding none type to 1 in conditions
        self.arr = [None] * self.size
    
    def enqueFront(self, element): # ! check all code for this method, like the if statements and algorithm/its order too (espeically inserting the element part and if/elif/else)
        if self.front == 0 and self.rear == self.size - 1 or self.front == self.rear + 1: # (overflow)
            return
        if self.front == -1: # ! check if correct (for empty condition)
            self.front = 0
        if self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        
        self.arr[self.front] = element
    
    def enqueRear(self, element):
        if self.front == 0 and self.rear == self.size - 1 or self.front == self.rear + 1: # (overflow)
            print('overflow')
            return
        if self.front == -1: # ! same check this if correct for empty condition
            self.rear = 0
        if self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        
        self.arr[self.rear] = element
    
    def dequeFront(self):
        if self.front == -1: # ! empty condition check
            self.front = None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else: self.front += 1
    
    def dequeRear(self):
        if self.front == -1: # ! empty condition check
            self.front = None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
    
    def display(self): # ! doesn't display all elements of the array
        print(self.arr)
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
    a = doubleEndedQueue(5)
    a.enqueFront(1)
    a.enqueFront(2)
    # a.enqueRear(1)
    # a.enqueRear(1)
    # a.enqueRear(1)
    # a.enqueRear(1)
    # a.enqueRear(2)
    a.dequeRear()
    a.dequeRear()
    a.display()

# ! check some things from algorithm in notes too
# ! any changes in display function for this type of queue from the circular?