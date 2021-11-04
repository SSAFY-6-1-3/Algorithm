import sys

sys.stdin = open('s_4789.txt')

def check(lst):
    people = lst[0]
    answer = 0

    for i in range(1, len(lst)):
        hired = 0
        if people < i:
            hired = i-people
            answer += hired
        people += lst[i] + hired

    return answer


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    print('#{} {}'.format(tc, check(lst)))