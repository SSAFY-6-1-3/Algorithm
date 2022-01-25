import sys

input = sys.stdin.readline

def solut(st):
    left, right = [], []

    for k in st:
        if k == '<':
            if left:
                right.append(left.pop())
        elif k == '>':
            if right:
                left.append(right.pop())
        elif k == '-':
            if left:
                left.pop()
        else:
            left.append(k)

    return ''.join(left + right[::-1])



N = int(input())
for _ in range(N):
    print(solut(input().strip()))