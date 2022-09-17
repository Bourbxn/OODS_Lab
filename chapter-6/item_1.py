def print1ToN(n):
    if n>0:
        if n-1>0:
            print1ToN(n-1)
        print(n,end=' ')
    else:
        print(1,end=' ')

def printNto1(n):
    if n>0:
        print(n,end=' ')
        if n-1>0:
            printNto1(n-1)
    else:
        print(1,end=' ')

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)
