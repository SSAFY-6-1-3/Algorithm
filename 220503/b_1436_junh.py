
N = int(input())

def is_ok(num):
    if '666' in str(num):
        return 1
    return 0

num = 666
cnt = 0

while cnt<N:
    if is_ok(num):
        cnt +=1
    num +=1


print(num-1)
# print(checked)
# print(checked[N-1])
