class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root:
            root = self.root
            while True:
                if data <= root.data:
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

    def print(self,root):
        if root:
            self.print(root.right)
            print(root.data, end=' ')
            self.print(root.left)

def sum_power(root):
    if not root:
        return 0
    return root.data + sum_power(root.left) + sum_power(root.right)

def sum_team(root):
    pass

def main():
    T = Tree()
    kn,vs = input("Enter Input : ").split('/')
    for i in kn.split():
        root = T.insert(int(i))
    T.printTree(root)
    print(sum_power(root))
    for i in vs.split(','):
        t1,t2 = i.split()
        print(f"{t1}?{t2}")

if __name__ == '__main__':
    main()
