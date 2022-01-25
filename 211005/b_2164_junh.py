from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
cards = deque(range(1, N+1))

while cards.__len__() >1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards.pop())