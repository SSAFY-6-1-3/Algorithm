from collections import deque

def check_paper(paper):
    clr = paper[0][0]
    length = len(paper)

    breaked = False         # 이중 포문을 한 번에 벗어나기 위한 토글
    for y in range(length):
        for x in range(length):
            if paper[y][x] != clr:      # 다른 색이 있으면
                paper_ul, paper_ur, paper_dl, paper_dr = split_paper(paper, length//2) # 함수를 통해 종이를 자르고
                check_paper(paper_ul)       # 각각 재귀
                check_paper(paper_ur)
                check_paper(paper_dl)
                check_paper(paper_dr)
                breaked = True              # 밖에서도 break 걸 수 있도록
                break
        if breaked:
            break
    else:
        result[clr] += 1                    # 다른 색이 없었으면 그 색의 숫자를 +1

def split_paper(paper, half):
    paper_u = paper[:half]          # 일단 위, 아래 반으로 자르고
    paper_d = paper[half:]
    paper_ul, paper_ur, paper_dl, paper_dr = [], [], [], []
    for r in range(half):           # 다시 옆으로 자른다
        paper_ul.append(paper_u[r][half:])
        paper_ur.append(paper_u[r][:half])
        paper_dl.append(paper_d[r][half:])
        paper_dr.append(paper_d[r][:half])
    return paper_ul, paper_ur, paper_dl, paper_dr


N = int(input())
org_paper = [list(map(int, input().split(' '))) for _ in range(N)]
result = [0, 0]
check_paper(org_paper)
print(result[0])
print(result[1])