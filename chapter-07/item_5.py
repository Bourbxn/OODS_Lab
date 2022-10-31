'''
ส่วนไหน
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root:
            root = self.root
            while True:
                if data < root.data:
                    if not root.left:
                        root.left = node
                        break
                    root = root.left
                else:
                    if not root.right:
                        root.right = node
                        break
                    root = root.right
        else:
            self.root = node
        return self.root

    def isExist(self,root,data):
        if data == root.data:
            return True
        if not root.left and not root.right:
            return False
        if data < root.data:
            return self.isExist(root.left, data)
        return self.isExist(root.right, data)

    def checkpos(self,data):
        if data == self.root.data:
            print("Root")
        elif data == self.root.left.data or data == self.root.right.data:
            print("Inner")
        elif self.isExist(self.root,data):
            print("Leaf")
        else:
            print("Not exist")
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])

