import math

def isPrime(number):
    for p in range(2, int(math.sqrt(number)) + 1):
        if not number % p:
            return False
    return True


def solution(n, k):
    answer = 0
    num = ''
    while n != 0:
        (n, m) = divmod(n, k)
        num += str(m)
    k_num = num[::-1]

    number = ''
    for i in k_num:
        if i != '0':
            number += i
        else:
            if int(number) > 1:
                if isPrime(int(number)):
                    answer += 1
            number = '0'
    if int(number) > 1:
        if isPrime(int(number)):
            answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))