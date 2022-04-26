# for문 돌면서 IOI이면 개수 세주기
N = int(input())
M = int(input())
words = input()

i, ans, temp = 0, 0, 0
while i < M-2:
    if words[i] == 'I' and words[i+1] == 'O' and words[i+2] == 'I':
        temp += 1
        if temp == N:
            ans += 1
            temp -= 1
        i += 1          # 'IOI'일 경우 두 칸씩 이동
    else:
        temp = 0
    i += 1              # 한 칸씩 이동

print(ans)