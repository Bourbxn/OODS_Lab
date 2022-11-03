'''
กล่องสินค้า
'''
def min_weight(w: list, n: int) -> int:
    if n==1:
        return sum(w)
    min_w = 10e10
    for i in range(len(w)):
        if len(w[i:]) < n-1:
            break
        cur_n = sum(w[:i])
        nxt_n = min_weight(w[i:],n-1)
        min_w = min(max(cur_n,nxt_n),min_w)
    return min_w

def main():
    inp = input("Enter Input : ").split('/')
    w, n = list(map(int, inp[0].split())),int(inp[1])
    print(f"Minimum weigth for {n} box(es) = {min_weight(w,n)}")

if __name__ == '__main__':
    main()