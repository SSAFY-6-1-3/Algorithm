sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

l, s = 0, 0
for w, h in sizes:
    maxv = max(w, h)
    minv = min(w, h)
    if maxv > l:
        l = maxv
    if minv > s:
        s = minv

print(l * s)