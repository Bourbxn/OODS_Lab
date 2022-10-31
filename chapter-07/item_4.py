'''
สนุกไปกับ Binary Search Tree
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

    def printPreorder(self, root):
        if root:
            print(root, end=' ')
            self.printPreorder(root.left)
            self.printPreorder(root.right)
    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root, end=' ')
            self.printInorder(root.right)

    def printPostorder(self, root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print(root, end=' ')

    def printBreadth(self, root, l = []):
        if root:
            print(root, end=' ')
            l.append(root.left) if root.left else 0
            l.append(root.right) if root.right else 0 
            self.printBreadth(l.pop(0),l) if len(l) else 0
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def main():
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = T.insert(i)
    travel = { 
            0:print("Preorder : ",end='') or T.printPreorder(root) or print(), 
            1:print("Inorder : ",end='') or T.printInorder(root) or print(),
            2:print("Postorder : ",end='') or T.printPostorder(root) or print(),
            3:print("Breadth : ",end='') or T.printBreadth(root) or print()
            }
    [i for i in travel]
 
if __name__ == '__main__':
    main()
