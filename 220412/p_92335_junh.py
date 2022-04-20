# def era(n):
#     prms = [True] * (n+1)
#     prms[0], prms[1] = False, False
#     maxi = int(n**0.5)
#
#     for i in range(2, maxi+1):
#         if prms[i]:
#             for j in range(i*2, n+1, i):
#                 prms[j] = False
#     return prms

def is_prime(n):
    if n<2: return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

def solution(n, k):
    answer = 0

    st = ''
    while n:
        st += str(n % k)
        n //= k
    st = st[::-1]

    for spl in st.split('0'):
        if spl and is_prime(int(spl)):
            answer+=1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))