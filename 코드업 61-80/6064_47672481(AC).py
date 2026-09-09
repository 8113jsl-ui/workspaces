a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(a if ((a <= b) and (a <= c)) else b if ((b <= a) and (b <= c)) else c)
