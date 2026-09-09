n = int(input())
number = input().split()
min = int(number[0])

for i in range(n):
    if min < int(number[i]):
        min = min
    else:
        min = int(number[i])
        

print(min)
