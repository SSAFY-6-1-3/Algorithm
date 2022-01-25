import sys

input = sys.stdin.readline

def make(length, lengths):
    result = 0
    for line in lines:
        result += line//length

    if result >= N:
        lengths.append(length)
        return True
    return False

def bin_search(l, r):
    if l>r: return
    mid = (l+r)//2

    if make(mid, lengths):
        bin_search(mid+1, r)
    else:
        bin_search(l, mid-1)


K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
lengths = [1]
bin_search(1, max(lines))
print(max(lengths))