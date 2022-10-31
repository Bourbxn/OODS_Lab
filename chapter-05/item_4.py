'''
VIM Text Editor
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

    def search(self,data):
    	pos = 0
    	found = False
    	temp = self.head
    	while temp:
    		if temp.data == '|':
    			found = True
    			break
    		pos+=1
    		temp=temp.next
    	return pos if found else -1

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
            return None
        else:
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
                result += " " + str(node.data)
                node = node.next
        else:
            result = ""
        return result

def main():
	dll = DoublyLinkedList()
	inp = input("Enter Input : ").split(',')
	for i in inp:
		key = i.split()[0]
		if key == 'I':
			data = i.split()[1]
			curp = dll.search('|')
			if curp == dll.size-1:
				dll.append(data)
				dll.remove('|')
				dll.append('|')
			else:
				dll.remove('|')
				dll.insert(curp,data)
				dll.insert(curp+1,'|')
		elif key == 'L':
			curp = dll.search('|')-1
			if curp >= 0 and dll.size>1:
				dll.remove('|')
				dll.insert(curp,'|')
		elif key == 'R':
			curp = dll.search('|')+1
			if curp < dll.size and dll.size>1:
				dll.remove('|')
				dll.insert(curp,'|')
		elif key == 'B':
			curp = dll.search('|')-1
			temp = dll.head
			for i in range(curp):
				temp=temp.next
			if dll.size > 1 and dll.search('|')>0:
				dll.remove(temp.data)
		elif key == 'D':
			curp = dll.search('|')+1
			temp = dll.head
			for i in range(curp):
				temp=temp.next
			if not dll.search('|')==dll.size-1:
				dll.remove(temp.data)
	print(dll)


if __name__ == '__main__':
	main()
