# [2번 문제] 
# 정수 2개를 입력받아서 큰 수와 작은 수를 차례로 출력하는 프로그램을 작성하시오.

# 1. 정수를 2개를 입력 - int(input())
num1 = int(input())
num2 = int(input())

# 2. 큰 수, 작은 수 비교 - if 구문으로 비교
# 3. 출력 - "입력받은 수 중 큰 수는 9이고 작은 수는 2입니다."
if num1 > num2:
    print("입력받은 수 중 큰 수는 " + str(num1) + "이고 작은 수는 " + str(num2) + "입니다.")
elif num1 < num2:
    print("입력받은 수 중 큰 수는 " + str(num2) + "이고 작은 수는 " + str(num1) + "입니다.")
elif num1 == num2:
    print("입력하신 두 수는 같습니다.")
else:
    print("입력값 오류")