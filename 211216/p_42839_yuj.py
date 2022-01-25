# 소수 확인하는 함수
# def isPrime(N):
#     if N < 2:
#         return 0
#     for i in range(2, N // 2 + 1):
#         if not N % i:
#             return 0
#     else:
#         return 1

#에라토스테네스의 체
total = [0, 0] + [1] * 10000000
for i in range(2, 10000001):
    if total[i]:
        for j in range(2*i, 10000001, i):
            total[j] = 0

def solution(numbers):
    nums = []
    result = []
    for number in numbers:
        nums.append(number)


    def perm(num, l):
        if len(num) == l:
            if int(num) not in result and total[int(num)]:
                result.append(int(num))
            return

        for j in range(len(nums)):
            if not visited[j]:
                visited[j] = 1
                perm(num+nums[j], l)
                visited[j] = 0


    for l in range(1, len(numbers)+1):
        visited = [0] * len(nums)
        perm('', l)

    print(result)
    return len(result)

numbers="17"
print(solution(numbers))