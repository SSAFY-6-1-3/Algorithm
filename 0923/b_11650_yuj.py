import sys
sys.stdin = open('input.txt')

# 병합 정렬 사용
def merge_sort(lst):
    # 리스트 쪼개기
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    # 리스트 순서대로 붙이기
    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l][0] < right[h][0]:            # [x, y]에서 x부터 비교
            merged_arr.append(left[l])
            l += 1
        elif left[l][0] > right[h][0]:
            merged_arr.append(right[h])
            h += 1
        else:                                   # x가 같다면 y 비교
            if left[l][1] <= right[h][1]:
                merged_arr.append(left[l])
                l += 1
            elif left[l][1] > right[h][1]:
                merged_arr.append(right[h])
                h += 1
    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr


N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])

result = merge_sort(lst)
for x, y in result:
    print (x, y)