import sys

def enq(num):
    global last
    last += 1

    # 인덱스 1 늘려주고, 맨 마지막 노드에 해당 번호 입력
    heap[last] = num

    child = last
    parent = child // 2

    while parent >= 1:
        # 자식노드가 부모노드보다 작으면 부모노드와 위치 바꾸기
        if abs(heap[child]) < abs(heap[parent]) or (abs(heap[child]) == abs(heap[parent]) and heap[child] < heap[parent]):
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2

        else:
            break


def deq():
    global last

    if last == 0:  # 빈 리스트면 0 출력
        print(0)
        return

    print(heap[1])
    heap[1] = 0
    heap[1] = heap[last]  # 맨 마지막 노드를 루트로 가져오기
    last -= 1
    parent = 1
    child = parent * 2  # 왼쪽 자식 노드 인덱스 번호로 설정

    while child <= last:  # 범위 내에서 체크
        if child + 1 <= last:  # 오른쪽 자식 노드가 있는 경우,
            # 왼쪽보다 오른쪽 자식이 작은 경우 오른쪽 자식노드 인덱스로 변경
            if abs(heap[child + 1]) < abs(heap[child]) or (abs(heap[child + 1]) == abs(heap[child]) and heap[child + 1] < heap[child]):
                child += 1

        # 자식노드가 부모노드보다 작은 경우, 위치 변경
        if abs(heap[child]) < abs(heap[parent]) or (abs(heap[child]) == abs(heap[parent]) and heap[child] < heap[parent]):
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2

        else:
            break





N = int(input())
heap = [0] * (N + 1)
last = 0

for _ in range(N):

    x = int(sys.stdin.readline())
    if x == 0:
        deq()
    else:
        enq(x)


