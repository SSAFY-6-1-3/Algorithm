import sys
sys.stdin=open('input.txt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def seq(result):
    if len(result) == M:
        print(*result)
        return

    for num in lst:
        if not result:
            seq(result+[num])
        elif result[-1] <= num:
            seq(result+[num])

seq([])