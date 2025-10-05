class stack:
    def __init__(self,cap):
        self.cap = cap
        self.top = -1
        self.arr = [0]*cap  
    #function for empty
    def is_empty(self):
        return self.top==-1
    
    def is_full(self):
        return self.top == self.cap-1 
    
    def push(self,element):
        if self.is_full():
            print("STACK OVERFLOW")
            return False
        else:
            self.top+=1
            self.arr[self.top] = element
            return True
    def pop(self):
        if self.is_empty():
            return False
        else:
            popped = self.arr[self.top]
            self.top-=1
            self.arr.pop()
            # print(popped)
    
    def display(self):
        # print(self.arr)
        return self.arr

    def peek(self):
        if self.arr.count(0) != len(self.arr):
            return self.arr[self.top]
        else: print('stack empty')



# function for full

#function for push


#function for pop



#function for peek



#function for display (traversing the array)

if '__main__':
    # s = stack(5)
    # s.push(10)
    # s.push(12)

    # s.display()
    # s.pop()
    # s.peek()

    #making queue with 2 stacks
    a = stack(4) # step 1: create 2 stacks
    b = stack(4)

    print('start input:')
    [(a.push(x), print(x)) for x in range(1, 5)] # step 2: insert elements in first stack
    # a.push(2)
    # a.push(5)
    # a.push(123)

    [(b.push(a.display()[-1]), a.pop()) for x in range(len(a.display()))] # step 3: pop from first and insert in second stack
    
    print('end output:')
    extras = b.arr.count(0)
    [print(b.display()[len(b.display()) - x - 1]) for x in range(len(b.display())-extras)]
    print('First in (1) was First out (1)')
    
    [b.pop() for x in range(len(b.display())-extras+1)] # step 4: pop elements
    print(b.display(), ': new second stack (everything taken out)')

    #to search insidew stacks, you would take from tail cosntantly until found desired elemet