d1, d2, d3 = map(int, input().split())

d = 1
while d%d1 != 0 or d%d2 != 0 or d%d3 != 0:
    d += 1

print(d)
