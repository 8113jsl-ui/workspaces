# [6번 문제] - swap 문제

# 정수 3개를 입력 받아 그중 가장 큰 수를 출력하는 프로그램을 작성하시오. 
# 출력 조건)  입력을 받기 전 "세 수를 입력하세요. "을 출력한다.
# 입력을 받은 후 "입력받은 수 중 가장 큰 수는 {가장 큰 수}입니다."를 출력한다.


# 1. 3개 input()
# 2. if 조건문으로 가장 큰 수 필터링
# 3. print(최대값) - "입력받은 수 중 가장 큰 수는 {가장 큰 수}입니다."

int1 = int(input())
int2 = int(input())
int3 = int(input())

if ((int1 - int2) >= 0) and ((int1 - int3) >= 0):
    print("입력받은 수 중 가장 큰 수는 " + str(int1) + "입니다.")
elif ((int2 - int1) >= 0) and ((int2 - int3) >= 0):
    print("입력받은 수 중 가장 큰 수는 " + str(int2) + "입니다.")
elif ((int3 - int1) >= 0) and ((int3 - int1) >= 0):
    print("입력받은 수 중 가장 큰 수는 " + str(int3) + "입니다.")


int1 = int(input())
int2 = int(input())
int3 = int(input())

if (int1 >= int2) and (int1 >= int3):
    print("입력받은 수 중 가장 큰 수는 " + str(int1) + "입니다.")
    print(f"{int1}입니다.")
elif (int2 >= int1) and (int2 >= int3):
    print("입력받은 수 중 가장 큰 수는 " + str(int2) + "입니다.")
    print(f"{int2}입니다.")
elif (int3 >= int1) and (int3 >= int2):
    print("입력받은 수 중 가장 큰 수는 " + str(int3) + "입니다.")
    print(f"{int3}입니다.")



int1 = int(input())
int2 = int(input())
int3 = int(input())

if int1 >= int2:
    if int1 >= int3:
        print("입력받은 수 중 가장 큰 수는 " + str(int1) + "입니다.")
        print(f"{int1}입니다.")

if int2 >= int1:
    if int2 >= int3:
        print("입력받은 수 중 가장 큰 수는 " + str(int2) + "입니다.")
        print(f"{int2}입니다.")

if int3 >= int1:
    if int3 >= int2:
        print("입력받은 수 중 가장 큰 수는 " + str(int3) + "입니다.")
        print(f"{int3}입니다.")



# 4. {가장 큰 수}입니다. 를 출력한다.

### print({}.format(가장 큰 수))
### print('{} 입니다'.format(가장 큰 수))
### print(f"{가장 큰 수}입니다.")