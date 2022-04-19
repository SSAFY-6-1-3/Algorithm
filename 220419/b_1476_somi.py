val = input()

E, S, M = 0, 0, 0
for i in range(1, 7981):
    E += 1
    if E == 16:
        E = 1

    S += 1
    if S == 29:
        S = 1

    M += 1
    if M == 20:
        M = 1

    y = str(E) + ' ' + str(S) + ' ' + str(M)

    if y == val:
        print(i)
        break

