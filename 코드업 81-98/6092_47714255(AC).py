n = int(input())
number = input().split()

for i in range(n):
    number[i] = int(number[i])

list = []
for i in range(24) : 
    list.append(0)  # 1 ~ 23 각 숫자의 횟수를 0으로 시작

for i in range(n):
    list[number[i]] += 1

for i in range(1, 24):
    print(list[i], end=' ')
