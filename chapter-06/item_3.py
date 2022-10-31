'''
( 2^(input) ) - 1
'''
def comb_bin(n,z):
    if n>0:
        comb_bin(n-1,z)
        print(bin(n)[2:].zfill(z))
    elif n==0:
        print(bin(0)[2:].zfill(z))
    else:
        print("Only Positive & Zero Number ! ! !")

def main():
    n = 2**int(input("Enter Number : "))-1
    z = len(str(bin(n)[2:])) if n>=0 else 0
    comb_bin(n,z)

if __name__ == '__main__':
    main()

