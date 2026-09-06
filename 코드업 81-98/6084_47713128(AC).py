h, b, c, s = map(int, input().split())

storage = h * b * c * s / 8 / 1024 / 1024

print(str(round(storage, 1)), "MB")
