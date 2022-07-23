N = int(input())
lst = []
for _ in range(N):
    serial = input()
    temp = list(map(str, serial))
    s = 0
    for t in temp:
        if t.isdigit() == True:
            s += int(t)
    lst.append((serial, s))

lst.sort(key=lambda x: (len(x[0]), x[1], x[0]))
for i in range(N):
    print(lst[i][0])
