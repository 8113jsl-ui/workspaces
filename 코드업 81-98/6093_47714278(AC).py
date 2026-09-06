n = int(input())
number = input().split()

list = []
for i in range(n):
    number[i] = int(number[i])
    list.append(number[i])

list_reverse = []
for j in range(n-1, -1, -1):
    list_reverse.append(list[j])

for k in range(n):
    print(list_reverse[k], end = " ")
