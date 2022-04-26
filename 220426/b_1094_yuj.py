X = int(input())
sticks = [64]
ans = 0
while sum(sticks) > X:
    stick = min(sticks)
    sticks.remove(stick)
    for _ in range(2):
        sticks.append(int(stick//2))
    if stick == 2:
        break

for s in sticks:
    if X >= s:
        X -= s
        ans += 1
    if X == 0:
        break

print(ans)

# X = int(input())
# ans = 0
# stick = 64
# while X > 0:
#     if stick > X:
#         stick = stick // 2
#     else:
#         ans += 1
#         X -= stick
# print(ans)