# list_range01.py
# 리스트를 선언합니다.

array = [273, 32, 103, 57, 52]

# 리스트에 반복문을 적용합니다.
for i in range(len(array)):
    # 출력합니다.    
    print("{}번째 반복:{}".format(i, array[i]))



# reversed_for01.py
# 역반복문
for i in range(4, 0 - 1, -1):
    # 출력합니다.    
    print("현재 반복 변수:{}".format(i))


# reversed_for02.py
# 역반복문
for i in reversed(range(5)):    
# 출력합니다.    
    print("현재 반복 변수:{}".format(i))



# * 연산자 사용
for i in range(1,10):
    print("*"*i)


# 결과값에서, 규칙 찾기!

# 넓이 = 면의 크기
# 면적 = 담을 수 있는 크기

# [규칙]
# 1. 한 줄씩 띄우기
# 2. * 가 1개씩 증가
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********

# for i in range(1,10):
#     for count in range(1,10):
#         print("\n" + "*")


# for_pyramid01.py
output = ""

for i in range(1, 10):
    for j in range(0, i):       ## j를 안 써도 된다!
            output += "*"       # 문자열 += : 붙여쓰기로 합쳐짐!!!!!  
    output += "\n"
    
print(output)



#     *
#    ***
#   *****

# [규칙]
# 1. \n 가 1씩 증가 ("\n" += 1)
# 2. 공백 : 2개 -> 1개 -> 0개 (-= 2)
# 3. * : 1개 -> 3개 -> 5개 (+= 2)
# 4. *이 중앙에 있음

pyramid = ""            # pyramid는 (공백) + * = (공백)*

# 줄 바꿈
for i in range(1,4):
    pyramid += "\n"
    # * 조건
    for j in range(1,6):
        pyramid += "*"

        # 공백 조건
        for k in range(1,3):
            pyramid -= " "


print(pyramid)
        