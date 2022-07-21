# 전위순회
def preorder(node):
    global result
    result += node
    if dic[node]:
        if dic[node][0].isalpha():
            preorder(dic[node][0])
        if dic[node][1].isalpha():
            preorder(dic[node][1])

# 중위순회
def inorder(node):
    global result

    if dic[node]:
        if dic[node][0].isalpha():
            inorder(dic[node][0])
        result += node
        if dic[node][1].isalpha():
            inorder(dic[node][1])
    else:
        result += node

# 후위순회
def postorder(node):
    global result

    if dic[node]:
        if dic[node][0].isalpha():
            postorder(dic[node][0])

        if dic[node][1].isalpha():
            postorder(dic[node][1])
    result += node

N = int(input())
dic = dict()
result = ''
for _ in range(N):
    m, l, r = map(str, input().split())
    dic[m] = [l, r]

preorder('A')
print(result)
result = ''

inorder('A')
print(result)
result = ''

postorder('A')
print(result)