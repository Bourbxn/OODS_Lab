'''
AVL ( Insert Only )
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            self.root = Node(data)
            return self.root
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)
        if balance < -1 and data >= root.right.data:
            return self.leftRotate(root)
        if balance > 1 and data >= root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
 
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def main():
    avl = AVL()
    inp = list(map(int, input("Enter Input : ").split()))
    root = None
    for i in inp:
        root = avl.insert(root,i)
        print(f"Insert : ( {i} )")
        avl.printTree(root)
        print("--------------------------------------------------")

if __name__ == '__main__':
    main()
