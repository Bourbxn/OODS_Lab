'''
First Greater Value
'''
def fgv_search(l: list,key: int,maxk: int = 10e6) -> str:
    if key >= maxk:
        return "No First Greater Value"
    if key in l:
        return str(key) 
    return fgv_search(l,key+1,maxk)

def main():
    inp = input("Enter Input : ").split('/')
    l, key = list(map(int, inp[0].split())), \
        list(map(int, inp[1].split()))
    for i in key:
        print(fgv_search(l,i+1,max(l)))

if __name__ == '__main__':
    main()