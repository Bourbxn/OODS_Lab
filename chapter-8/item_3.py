'''
Ranking
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

    def ranking(self,root,data):
        if not root:
            return 0
        rank = 0
        rank += 1 if data >= root.data else 0
        rank += self.ranking(root.left, data)
        rank += self.ranking(root.right,data)
        return rank
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def main():
    T = BST()
    inp = input("Enter Input : ").split('/')
    for i in inp[0].split():
        root = T.insert(int(i))
    T.printTree(root)
    print("--------------------------------------------------")
    print(f"Rank of {inp[1]} : {T.ranking(root,int(inp[1]))}")

if __name__ == '__main__':
    main()
