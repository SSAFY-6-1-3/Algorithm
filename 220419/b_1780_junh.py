N = int(input())
papers = [[list(map(int, input().split())) for _ in range(N)]]
answer = 0

def sol(papers):


def is_ok(paper):
    li = []
    for r in paper:
        li.extend(r)
    if len(set(li)) == 1:
        return True
    return False

for paper in papers:
    if not is_ok(paper):





