print(10 / 5)
print(10 // 3)
print(10 % 3)

int("52.5")

print("점수: " + 90)

n = int(input())

total = 0
i = 0

while total < n:
    i += 1
    total += i

    if total >= n:
        break

print(i)




p = int(input())

total = 0

for i in range(1, p+1):
    total += i

    if total >= p:
        break

print(i)



n, m = map(int, input().split())

for i in range(1, n+1):
	for j in range(1, m+1):
          print(i, j)



a = input()

for i in range(1,int(a, 16)):
     a_1 = '%X'%int(a, 16)
     i_1 = '%X'%i
     print('{}*{}={}'.format(int(a_1,16), int(i_1,16), hex(int(a_1,16) * int(i_1,16))))