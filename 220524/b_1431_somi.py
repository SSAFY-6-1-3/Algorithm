N = int(input())
guitars = []
for _ in range(N):
    guitar = input()
    num = [int(i) for i in guitar if i.isdigit()]
    guitars.append((guitar, sum(num)))

guitars.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for guitar in guitars:
    print(guitar[0])

