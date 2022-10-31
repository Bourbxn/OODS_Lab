'''
Doubly Linked List(append,insert,remove)
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head

    def append(self, data):
        node = Node(data)
        if self.tail:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def insert(self, index, data):
        node = Node(data)
        if index==self.size or self.size==0:
            self.size-=1
            self.append(data)
        elif index==0:
            if self.tail:
                node.next = self.head
                self.head.previous = node
                self.head = node
            else:
                self.head = node
                self.tail = node
        else:    
            temp = self.head
            for i in range(index-1):
                if temp:
                    temp = temp.next
            tempprev = self.tail
            for i in range(self.size-1,index,-1):
                if tempprev:
                    tempprev = tempprev.previous
            if temp or tempprev:
                node.next = temp.next
                node.previous = tempprev.previous
                temp.next = node
                tempprev.previous = node
        self.size += 1

    def remove(self,data):
        temp = self.head
        isin = False
        index = 0
        while temp:
            if temp.data == data and temp == self.head:
                isin = True
                if not temp.next:
                    temp = None
                    self.head = None
                    self.tail = None
                    break
                else:
                    nxt = temp.next
                    temp.next = None
                    nxt.previous = None
                    temp = None
                    self.head = nxt
                    break
            elif temp.data == data:
                isin = True
                if temp.next:
                    nxt = temp.next
                    prev = temp.previous
                    prev.next = nxt
                    nxt.previous = prev
                    temp.next = None
                    temp.previous = None
                    temp = None
                    break
                else:
                    prev = temp.previous
                    prev.next = None
                    temp.previous = None
                    temp = None
                    self.tail = prev
                    break
            temp = temp.next
            index += 1
        if not isin:
            print("Not Found!")
            return None
        else:
            print(f'removed : {data} from index : {index}')
            self.size -= 1
            return data

    def str_reverse(self):
        result = str()
        node = self.tail
        if node:
            result += str(node.data)
            node = node.previous
            while node:
                result += "->" + str(node.data)
                node = node.previous
        else:
            result = ""
        return result

    def __str__(self):
        result = str()
        node = self.head
        if node:
            result += str(node.data)
            node = node.next
            while node:
                result += "->" + str(node.data)
                node = node.next
        else:
            result = ""
        return result

def main():
    inp = input("Enter Input : ").split(',')
    linkedList = DoublyLinkedList()
    for i in inp:
        key,data = i.split()
        if key == 'A':
            linkedList.append(data)
        elif key == 'Ab':
            linkedList.insert(0,data)
        elif key == 'I':
            index, subdata = data.split(':')
            if int(index)<0 or int(index)>linkedList.size:
                print("Data cannot be added")
            else:
                print(f'index = {index} and data = {subdata}')
                linkedList.insert(int(index),subdata)
        elif key == 'R':
            linkedList.remove(data)
        print(f"linked list : {linkedList}")
        print(f"reverse : {linkedList.str_reverse()}")
        #print(f'size .. {linkedList.size}')
    

if __name__ == '__main__':
    main()

# Enter Input : A 3,A 4,Ab 0,I 1:2
# linked list : 3
# reverse : 3
# linked list : 3->4
# reverse : 4->3
# linked list : 0->3->4
# reverse : 4->3->0
# index = 1 and data = 2
# linked list : 0->2->3->4
# reverse : 4->3->2->0
