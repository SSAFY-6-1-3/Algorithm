# import sys
#
# input = sys.stdin.readline

def calc(cnt, rst):
    if cnt == N:
        results.append(rst)
        return
    for c in range(4): # 연산자를 도는 for문
        if C_li[c]: # 그 연산자의 숫자가 0이 아니면 사용
            C_li[c] -= 1 # 사용했으므로 -1
            n_rst = rst # 새 결과를 저장할 변수
            # 연산자에 알맞은 결과를 n_rst에 저장
            if c == 0:
                n_rst += A_li[cnt]
            elif c == 1:
                n_rst -= A_li[cnt]
            elif c == 2:
                n_rst *= A_li[cnt]
            elif c == 3: # 나누기를 음수에서도 나머지를 버리는 나눗셈으로 적용
                n_rst /= A_li[cnt]
                n_rst = int(n_rst)
            calc(cnt + 1, n_rst) # 새 결과를 사용해 다시 재귀
            C_li[c] += 1 # 재귀가 끝난 뒤에 다시 연산자를 사용할 수 있도록 +1



N = int(input())
A_li = list(map(int, input().split())) # 숫자들의 리스트
C_li = list(map(int, input().split())) # 연산자들의 리스트
results = []
calc(1, A_li[0])
results.sort()
print(results[-1])
print(results[0])