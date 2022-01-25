from math import gcd
def solution(w, h):
    k = gcd(w, h)
    x = w // k
    y = h // k

    ans = w * h - (x + y - 1) * k
    return ans