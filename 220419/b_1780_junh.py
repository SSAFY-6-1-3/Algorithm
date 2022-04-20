N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
dic = {0:0, 1:0, -1:0}


def check(paper):
    li = []
    for r in paper:
        li.extend(r)
    if len(set(li)) == 1:
        dic[li[0]] += 1
    else:
        size = len(paper)//3
        for r in range(3):
            for c in range(3):
                pap = [paper[r * size+i][c * size:(c + 1) * size] for i in range(size)]
                check(pap)

check(paper)
print(dic[-1])
print(dic[0])
print(dic[1])


