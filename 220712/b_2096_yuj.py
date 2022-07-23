N = int(input())
lst = list(map(int, input().split()))
maxv, minv = lst, lst
temp1, temp2 = [0] * 3, [0] * 3

for i in range(N-1):
    matrix = list(map(int, input().split()))

    temp1[0] = matrix[0] + max(maxv[0], maxv[1])
    temp1[1] = matrix[1] + max(maxv)
    temp1[2] = matrix[2] + max(maxv[2], maxv[1])
    maxv = temp1[:]

    temp2[0] = matrix[0] + min(minv[0], minv[1])
    temp2[1] = matrix[1] + min(minv)
    temp2[2] = matrix[2] + min(minv[2], minv[1])
    minv = temp2[:]

print(max(maxv), min(minv))