
def check(heights):
    answer = 0
    l = 0
    while l < len(heights):
        left = heights[l]
        r = l+1
        right = 0

        for i in range(l+1, len(heights)):
            if right < heights[i]:
                r = i
                right = heights[i]
            if right >= left:
                break

        dam = min(left, right)
        for i in range(l+1, r):
            answer += dam - heights[i]

        l = r
    return answer

h, w = map(int, input().split())
heights = list(map(int, input().split()))
print(check(heights))