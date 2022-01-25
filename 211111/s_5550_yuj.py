import sys
sys.stdin=open('sample_input.txt')

def find(words):
    frogs = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    cnt = 0

    for idx in range(len(words)):
        word = words[idx]
        frogs[word] += 1

        for alpha in range(1, 5):               # croak 각각의 알파벳 수가 증가하는 형태여야 함
            if frogs[frog[alpha-1]] < frogs[frog[alpha]]:
                return -1

        if word == 'c':
            if cnt > 0:                         # 완성된 개구리가 존재했었다면 예전 개구리가 울었다고 생각 -> 최소 개구리수
                cnt -= 1

        if word == 'k':                         # 개구리 한 마리 완성
            cnt += 1

    if frogs['c'] == frogs['k']:                # 'ccroak'의 경우 -1로 return
        return cnt
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    frog = 'croak'
    words = input()

    print('#{} {}'.format(tc, find(words)))





