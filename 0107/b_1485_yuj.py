import math
def length(i, j):
    return math.sqrt((square[i][0]-square[j][0])**2 + (square[i][1]-square[j][1])**2)

T = int(input())
for _ in range(T):
    side = set()                    # 네 변의 길이 모두 add
    diag = set()                    # 두 대각선의 길이 모두 add
    square = []
    for _ in range(4):
        square.append(list(map(int, input().split())))

    square.sort()                  # sort하면 점 위치가 1 3 순서로 정렬
    side.add(length(0, 1))                          # 0 2
    side.add(length(0, 2))
    side.add(length(1, 3))
    side.add(length(2, 3))
    diag.add(length(1, 2))
    diag.add(length(0, 3))

    if len(side) == 1 and len(diag) == 1:
        print(1)
    else:
        print(0)