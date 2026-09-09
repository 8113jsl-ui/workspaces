w, h, b = map(int, input().split())

image = w * h * b / 8 / 1024 / 1024

print(f"{image:.2f} MB")
