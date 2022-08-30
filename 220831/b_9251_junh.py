str1 = input()
str2 = input()
dp = [[0 for _ in range(len(str2) + 1)]for _ in range(len(str1) + 1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])


# a = input()
# b = input()
#
# a_len = len(a)
# b_len = len(b)
#
# d = [0] * b_len
# for i in range(a_len):
# 	cnt = 0
# 	for j in range(b_len):
# 		if cnt < d[j]:
# 			cnt = d[j]
# 		elif a[i] == b[j]:
# 			d[j] = cnt + 1
# print(max(d))


