'''
รู้จักกับ Binary Search Tree
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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
