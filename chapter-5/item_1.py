'''
Insert ข้อมูลลงใน index ที่กำหนดของ Singly Linked List
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
        result = "link list : "
        node = self.head
        if node != None:
            result += str(node.data)
            node = node.next
            while node:
                result += "->" + str(node.data)
                node = node.next
        else:
            result = "List is empty"
        return result    


def main():
    txt = input("Enter Input : ").split(',')
    linkedList = LinkedList()
    for i in txt[0].split():
        linkedList.append(i)
    print(linkedList)
    for i in txt:
        if ':' in i:
            index = int(i.split(':')[0])
            data = i.split(':')[1]
            if index>=0 and index<=linkedList.size:
                print(f"index = {index} and data = {data}")
                linkedList.insert(index,data)
                print(linkedList)
            else:
                print("Data cannot be added")
                print(linkedList)

if __name__ == '__main__':
    main()