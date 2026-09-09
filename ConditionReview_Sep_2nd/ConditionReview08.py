# [8번 문제]

# 1. 정수 2개 입력 - input()
num1 = int(input())
num2 = int(input())

# 2. 조건연산자 if
if num1 > num2:
    print('더 큰 값은 {}입니다!'.format(num1))      # .format()
elif num1 < num2:
    print(f'더 큰 값은 {num2}입니다!')              # f'~~~' 구문
elif num1 == num2:
    print('동일한 숫자입니다 :)')