# import sys
#
# input = sys.stdin.readline

def calc(cnt, rst):
    if cnt == N:
        results.append(rst)
        return
    for c in range(4):
        if C_li[c]:
            C_li[c] -= 1
            n_rst = rst
            if c == 0:
                n_rst += A_li[cnt]
            elif c == 1:
                n_rst -= A_li[cnt]
            elif c == 2:
                n_rst *= A_li[cnt]
            elif c == 3:
                n_rst /= A_li[cnt]
                n_rst = int(n_rst)
            calc(cnt + 1, n_rst)
            C_li[c] += 1



N = int(input())
A_li = list(map(int, input().split()))
C_li = list(map(int, input().split()))
results = []
calc(1, A_li[0])
results.sort()
print(results[-1])
print(results[0])