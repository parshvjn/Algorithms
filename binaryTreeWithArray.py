
class tree:
    def __init__(self, size):
        self.size = size
        self.tree = [None]*(self.size + 1)
        self.last_index = 0

    def insert(self, value):
        if self.last_index >= self.size: return "tree is full"
        self.last_index += 1
        self.tree[self.last_index] = value
    
    def display(self):
        for i in range(1, self.size + 1):
            if self.tree[i] != None:
                left = self.tree[2*i] if 2*i <= self.size else None
                right = self.tree[(2*i) + 1] if (2*i) + 1 <= self.size else None
                print('root:', self.tree[i])
                print('left:', left, 'right:', right)
    
    def inorderTraverse(self, point = 1):
        if point <= self.last_index and self.tree[point] != None:
            self.inorderTraverse(2*point)
            print(self.tree[point], end = ' -> ')
            self.inorderTraverse(2*point + 1)

    def preorderTraverse(self, point = 1):
        if point <= self.last_index and self.tree[point] != None:
            print(self.tree[point], end = ' -> ')
            self.preorderTraverse(2*point)
            self.preorderTraverse(2*point + 1)

    def postorderTraverse(self, point = 1):
        if point <= self.last_index and self.tree[point] != None:
            self.postorderTraverse(2*point)
            self.postorderTraverse(2*point + 1)
            print(self.tree[point], end = ' -> ')

if '__main__':
    # alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F']
    treeFirst = tree(len(alphabets))
    for x in range(len(alphabets)):
        treeFirst.insert(alphabets[x])
    print('inorder: ')
    treeFirst.inorderTraverse()
    print('\npreorder: ')
    treeFirst.preorderTraverse()
    print('\npostorder: ')
    treeFirst.postorderTraverse()