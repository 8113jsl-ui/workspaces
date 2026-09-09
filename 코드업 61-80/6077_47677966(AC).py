n = int(input())

total = 0

for i in range(n + 1):
    if i % 2 == 0:
        total += i      # x += 3  =>  x = x + 3
                        # a += b  => a에 b만큼 누적해서 더함

print(total)
