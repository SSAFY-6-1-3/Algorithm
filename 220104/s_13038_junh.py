import sys

sys.stdin = open('s_13038_input.txt')

def solut(n, li):
    week_sum = sum(li)
    answer = 0
    if week_sum == 1:
        return (n-1)*7 + 1

    if n > week_sum:
        answer = (n//week_sum - 1) * 7
        n = n%week_sum + week_sum
    answer_rest = 14

    for start in range(7):
        if not li[start]: continue
        cnt = 0
        for i in range(14):
            day = (start+i)%7
            if li[day]:
                cnt +=1
                if cnt == n:
                    answer_rest = min(answer_rest, i+1)
                    break

    return answer + answer_rest

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))

    print('#{} {}'.format(tc, solut(n, li)))