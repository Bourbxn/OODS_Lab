'''
วาดภาพแสนสุข
'''
def staircase(n,r):
    if n>0:
        return '_'*(n-1) + '#'*(r-n+1) + '\n' + staircase(n-1,r)
    elif n<0:
        return '_'*(abs(r)-abs(n)) + '#'*(abs(n)) + '\n' + staircase(n+1,r) 
    else:
        return 'Not Draw!' if r==0 else ''

def main():
    n = int(input("Enter Input : "))
    r = n
    print(staircase(n,r))

if __name__ == '__main__':
    main()


