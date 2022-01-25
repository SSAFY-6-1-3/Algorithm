import sys
sys.stdin = open('s_2930.txt')

def add(num):
    global last
    last += 1  # 마지막을 늘리고
    tree[last] = num  # 맨 마지막에 삽입
    child = last
    parent = child // 2

    # 부모 노드와 비교해서 자식이 더 크면 바꾸기
    while parent >= 1 and tree[parent] < tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2


def delete():
    global last

    if tree[1] == 0:
        print('-1', end=' ')

    else:
        print(tree[1], end=' ')  # 루트 노드 프린트
        tree[1] = 0   # 루트 노드를 0으로 초기화
        tree[1] = tree[last]  # 루트 노드에 마지막 노드 저장
        last -= 1  # 마지막 인덱스 값 -1
        parent = 1

        # 수업시간에 배운건데.... 시간초과 ㅠㅠ
        # child_l = parent * 2
        # child_r = parent * 2 + 1
        #
        # while child_l <= last:
        #     if child_r <= last:
        #         if tree[child_l] > tree[child_r] and tree[child_l] > tree[parent]:
        #             tree[child_l], tree[parent] = tree[parent], tree[child_l]
        #             parent = child_l
        #         elif tree[child_r] > tree[child_l] and tree[child_r] > tree[parent]:
        #             tree[child_r], tree[parent] = tree[parent], tree[child_r]
        #             parent = child_r
        #         child_l = parent * 2
        #         child_r = parent * 2 + 1
        #     else:
        #         if tree[child_l] > tree[parent]:
        #             tree[child_l], tree[parent] = tree[parent], tree[child_l]
        #             break

        child = parent * 2
        while child <= last:  # 마지막 자식까지 확인해서 큰 값을 부모자리로 옮기기
            if child + 1 <= last and tree[child + 1] > tree[child]: # 오른쪽 노드가 있고, 오른쪽 노드가 왼쪽 노드보다 클 때
                child += 1  # 오른쪽 노드 확인하러 가기
            if tree[child] > tree[parent]: # 부모노드보다 자식 노드가 큰 경우
                tree[child], tree[parent] = tree[parent], tree[child] # 바꾸기
                parent = child  # 해당 노드의 자식 노드 확인하러 가기
                child = parent * 2
            else:
                break

T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    tree = [0] * (N + 1)
    last = 0
    for operation in data:
        if operation[0] == 1:
            add(operation[1])

        else:
            delete()
    print('')