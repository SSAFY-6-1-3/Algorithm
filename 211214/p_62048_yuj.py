from math import gcd

def solution(w, h):
    answer = (w * h) - (w + h - gcd(w, h))
    return answer

W, H = 8, 12
print(solution(W, H))