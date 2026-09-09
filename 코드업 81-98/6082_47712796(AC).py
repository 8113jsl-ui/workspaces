n = int(input())

for i in range(1, n+1):
    x_count = 0
    
    for j in range(len(str(i))):
        if (int(str(i)[j])%3 == 0) and (int(str(i)[j]) != 0):
            x_count += 1
    if x_count > 0:
        print("X" * x_count, end = " ")
    else:
        print(i, end = " ")
