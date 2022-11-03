'''
Rehashing
'''
class Data:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Hash:
    def __init__(self, t_size, max_coll, threshold):
        self.t_size = t_size
        self.max_coll = max_coll
        self.threshold = threshold
        self.dupl_table = list()
        self.table = [None for i in range(t_size)]
    
    def rehash_t_size(self,n: int) -> int:
        n *= 2
        while True:
            fac, n = 0, n+1
            for i in range(2, n):
                fac += 1 if n%i==0 else 0
                if fac>1:
                    break
            if fac == 0:
                break
        return n 

    def rehash_resize(self) -> None:
        self.t_size = self.rehash_t_size(self.t_size)
        self.table = [None for i in range(self.t_size)]
    
    def rehash_insert(self) -> None:
        for i in self.dupl_table:
            b_idx = idx = i%self.t_size
            coll = 0
            while self.table[idx]:
                coll+=1
                print(f"collision number {coll} at {idx}")
                if coll == self.max_coll:
                    break
                idx = (b_idx+coll**2)%self.t_size
            if not self.table[idx]:
                self.table[idx] = i

    def insert(self, val: int) -> None:
        print(f"Add : {val}")
        b_idx = idx = val%self.t_size
        coll = 0
        while self.table[idx]:
            coll += 1
            print(f"collision number {coll} at {idx}")
            if coll == self.max_coll:
                print("****** Max collision - Rehash !!! ******")
                self.rehash_resize() or self.rehash_insert()
                idx = val%self.t_size
                break
            idx = (b_idx+(coll**2))%self.t_size 
        self.dupl_table.append(val)
        if len(self.dupl_table)*100/self.t_size >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash_resize() or self.rehash_insert()
        else:
            self.table[idx] = Data(val)

    def __str__(self):
        s = str()
        for i,val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "----------------------------------------"

def main():
    print(" ***** Rehashing *****")
    inp = input("Enter Input : ").split('/')
    t_size, max_coll, threshold = int(inp[0].split()[0]),int(inp[0].split()[1])\
        ,int(inp[0].split()[2])
    hash = Hash(t_size,max_coll,threshold)
    print("Initial Table :")
    print(hash)
    for i in inp[1].split():
        hash.insert(int(i)) or print(hash)

if __name__ == '__main__':
    main()