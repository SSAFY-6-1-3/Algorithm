import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(T):
    nums = list(map(int, input().split()))
    answer = []
    for num in nums:
        temp = [int(i) for i in str(num)]
        answer.append(sum(temp))
    print('#{} {} {}'.format(tc, max(answer), min(answer)))