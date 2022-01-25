def gys(w, h):
    big, small = max(w, h), min(w, h)
    temp = 0

    while small:
        temp = big%small
        big, small = small, temp
    return big

def solution(w, h):
    return (w*h) - (w+h-gys(w, h))

print(solution(8, 12))

# def solution(w,h):
#     answer = 0
#     for i in range(w):
#         answer += h*i//w
#     return answer*2