def solution(n):
    n -=1
    for i in range(2, n+1):
       if not n%i:
           return i




print(solution(10))
print(solution(12))