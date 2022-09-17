'''
รวม Linked List
'''

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head

    def append(self,data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def insert(self,index,data):     
        node = Node(data)
        if index==self.size or self.size==0:
            self.append(data)
        elif index==0:
            node.next = self.head
            self.head = node
        else:    
          temp = self.head
          for i in range(index-1):
            if(temp != None):
              temp = temp.next   
          if(temp != None):
            node.next = temp.next
            temp.next = node
        self.size += 1
            

    def __str__(self):
        result = str()
        node = self.head
        if node != None:
            while node:
                result += " " + str(node.data)
                node = node.next
        else:
            result = "List is empty"
        return result

def create(l):
    ll = LinkedList()
    for i in l:
        ll.append(i)
    return ll

def merge(ll1,ll2):
    merge = LinkedList()
    merge = ll1
    for i in range(ll2.size)[::-1]:
        temp = ll2.head
        for i in range(i):
            temp = temp.next
        merge.append(temp.data)
    return merge

def main():
    l1inp,l2inp = input("Enter Input (L1,L2) : ").split()
    l1,l2 = l1inp.split('->'),l2inp.split('->')
    ll1,ll2 = create(l1),create(l2)
    print(f"L1    :{ll1}")
    print(f"L2    :{ll2}")
    print(f"Merge :{merge(ll1,ll2)}")



if __name__ == '__main__':
	main()

# Enter Input (L1,L2) : 1->2->3 4->5
# L1    : 1 2 3 
# L2    : 4 5 
# Merge : 1 2 3 5 4 
