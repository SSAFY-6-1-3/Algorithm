def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    change_to_k = ''
    while n > 0:
        n, mod = divmod(n, k)
        change_to_k = str(mod) + change_to_k

    for num in change_to_k.split('0'):
        if num and isPrime(int(num)):
            answer += 1

    return answer

print(solution(110011, 10))