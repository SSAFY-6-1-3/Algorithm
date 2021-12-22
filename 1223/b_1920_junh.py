N = int(input())
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))
A.sort()

def bin_search(l, r, target):
    m = (l+r) // 2
    if r<=l:
        print(0)
        return
    if A[m] == target:
        print(1)
        return

    if A[m] < target:
        bin_search(m+1, r, target)
    else:
        bin_search(l, m, target)

for b in B:
    bin_search(0, N, b)
