input = int(input())

for i in range(0, input):
    i += 1
    if i%3 == 0:
        continue
    else:
        print(i, end = " ")
