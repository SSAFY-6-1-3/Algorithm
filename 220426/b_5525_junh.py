N = int(input())
M = int(input())
S = input()
dic = {0:'I', 1:'O'}
P = 'I' + 'OI'*N
cnt = 0

def check(si, S):
    i = si
    cnt = 0
    while i < len(S) and S[i] == dic[(i-si)%2]:
        cnt+=1
        i+=1
    l = (i - si)//2
    if i==len(S) or S[i] =='O':
        l-=1
    IOs = l-N+1

    return IOs, cnt

IO = 0
i = 0
while i <= len(S) - len(P):
    if S[i] == 'I':
        IOs, cnt = check(i, S)
        if IOs > 0:
            IO += IOs
        i += cnt
    else:
        i += 1
print(IO)

# for i in range(len(S) - len(P)):
#     if S[i:i+len(P)] == P:
#         cnt +=1
#
# print(cnt)