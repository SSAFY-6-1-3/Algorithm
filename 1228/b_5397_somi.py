
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    left = []
    right = []
    pwd = input().strip()

    for i in pwd:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(right[::-1])
    print(''.join(left))


'''
index를 이동시키면서 해결 => 시간초과
def password(inpwd):
    # pwd = ['']
    pwd = []
    idx = 0
    for i in range(len(inpwd)):
        if inpwd[i] == '<' and idx > 0:
            idx -= 1

        elif inpwd[i] == '>' and idx < len(pwd):
            idx += 1

        elif inpwd[i] == '-' and idx > 0:
            pwd.pop(idx-1)
            idx -= 1

        elif inpwd[i].isalpha() or inpwd[i].isdigit():
            # if i and inpwd[i-1] == '>':
            #     pwd.insert(idx, inpwd[i])
            #     continue

            pwd.insert(idx, inpwd[i])
            idx += 1

    return pwd
'''








