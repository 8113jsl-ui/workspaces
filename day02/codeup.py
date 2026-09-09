number = int(input())

print(number - 1)
1 <= number <= 100
while (number - 1) != 0:
    number = number - 1
    print(number - 1)


alphabet = input()

end_num = ord(alphabet)
num = ord('a')

while num <= end_num:
    print(chr(num), end = " ")
    num = num + 1



num = int(input())
start_point = 0
end_point = num

print(start_point)
while start_point < end_point:
    start_point = start_point + 1
    print(start_point)


n = int(input())

total = 0

for i in range(n + 1):
    if i % 2 == 0:
        total += i      # x += 3  =>  x = x + 3
                        # a += b  => a에 b만큼 누적해서 더함
print(total)
    