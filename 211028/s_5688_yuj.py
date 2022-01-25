import sys
sys.stdin=open('sample_input.txt')

def binary_search(l, r):
    global result

    if l <= r:
        mid = (l+r) // 2

        if num[mid] == N:
            result = mid + 1
            return

        if l == r:
            return

        elif num[mid] > N:
            binary_search(l, mid-1)

        elif num[mid] < N:
            binary_search(mid+1, r)


T = int(input())
num = [i**3 for i in range(1, 10**6+1)]
for tc in range(1, T+1):
    N = int(input())
    result = -1
    binary_search(0, len(num))
    print('#{} {}'.format(tc, result))