

# def toC(java):
#     ret = ''
#
#     for c in java:
#         if c == '_': return "Error!"
#         if c.isupper():
#             ret += '_' + c.lower()
#         else:
#             ret += c
#     return ret
#
#
# def toJava(C):
#     ret = ''
#     i = 0
#     while i < len(C):
#         if C[i].isupper(): return "Error!"
#         if C[i] == '_':
#             i += 1
#             ret += C[i].upper()
#         else:
#             ret += C[i]
#         i += 1
#     return ret

st = input()

if st[0].isupper() or st[0] == '_':
    print("Error!")
    exit()


NoneCJava = 0 # 0:None 1:C++ 2:Java
ans = ''
i = 0
while i < len(st):

    if NoneCJava <= 1:
        if st[i] == '_':
            NoneCJava = 1
            i += 1
            if i >= len(st) or not st[i].islower():
                print('Error!')
                break
            ans += st[i].upper()

        elif st[i].isupper():
            if not NoneCJava:
                ans += '_' + st[i].lower()
                NoneCJava = 2
            else:
                print('Error!')
                break
        else:
            ans += st[i]

    elif NoneCJava == 2:
        if st[i].isupper():
            ans += '_' + st[i].lower()
        elif st[i].islower():
            ans += st[i]
        else:
            print('Error!')
            break

    i += 1

else:
    print(ans)

