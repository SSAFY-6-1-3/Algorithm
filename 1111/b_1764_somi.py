N, M = map(int, input().split())
never_heard = {input() for _ in range(N)}
never_seen = {input() for _ in range(M)}


ans = sorted(never_heard & never_seen)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])