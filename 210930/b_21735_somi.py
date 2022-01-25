'''
?? 왜 28???

'''


# dp = [1]
# time = 0
# location = 0
# while time < M:
#
#     plan_a = dp[-1] + a[location + 1]
#     plan_b = (dp[-1] // 2) + a[location + 2]
#     if plan_a >= plan_b:
#         dp.append(plan_a)
#         location += 1
#         print(location)
#     else:
#         dp.append(plan_b)
#         location += 2
#         print(location)
#
#     time += 1
#
#     if len(dp) == N + 1:
#          break
# print(dp[-1])

def make_snowball(location, ball, time):
    global max_snow_ball

    if time > M or location == N + 1:
        return

    if ball > max_snow_ball:
        max_snow_ball = ball

    if location <= N - 1:
        make_snowball(location + 1, ball + a[location + 1], time + 1)

    if location <= N - 2:
        make_snowball(location + 2, ball // 2 + a[location + 2], time + 1)


N, M = map(int, input().split())

a = [0] + list(map(int, input().split()))

max_snow_ball = 1
make_snowball(0, 1, 0)
print(max_snow_ball)