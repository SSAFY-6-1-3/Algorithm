def binarysearch(num, A, start, end):
    global flag

    if start <= end:
        mid = (start + end) // 2

        if A[mid] == num:
            flag = 1
            return

        if A[mid] > num:
            binarysearch(num, A, start, mid-1)

        elif A[mid] < num:
            binarysearch(num, A, mid+1, end)

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
for num in nums:
    flag = 0
    binarysearch(num, A, 0, N-1)
    print(flag)