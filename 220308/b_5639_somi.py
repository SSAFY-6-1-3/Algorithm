import sys
sys.setrecursionlimit(10**9)  # 재귀 깊이 길어지는 경우 에러 방지

def post(start, end):
    if start > end:
        return

    div = end + 1
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            div = i
            break
    post(start + 1, div - 1)
    post(div, end)
    print(tree[start])

tree = []
cnt = 0

while cnt < 10000:
    try:
        num = int(input())
    except:
        break

    tree.append(num)
    cnt += 1

post(0, len(tree) -1)