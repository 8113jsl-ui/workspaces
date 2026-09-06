p = int(input())

total = 0

for i in range(1, p+1):
    total += i

    if total >= p:
        break

print(i)
