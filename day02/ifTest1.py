print(10 <= 100)          # == != > < >= <= 비교연산자

print(True)
print(False)

print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)


# 문자열 비교 : Sorting을 위해서 함 (오름차순, 내림차순)
print("가방" == "가방")   # True
print("가방" != "하마")   # True
print("가방" < "하마")    # True (가방이 하마보다 작음)
print("가방" > "하마")    # False

x = 25
data = input("숫자를 입력하세요 > ")
print(10 < x < 30)
print(40 < x < 60)
print(type(data))
print(int(data) + 3)
print(float(data) + 3)
# print(data + 3)  # 문자열 + 숫자 => 에러 발생

# input() : input으로 받은 값은 기본적으로 문자열
# int(input()) : input으로 받은 값을 정수로 변환



print(True)
# print(!True) # not True => False

data2 = True
print(not data2)
print(not False)

x = 10
under_20 = x < 20  # under_20 = (x < 20)
print("under_20:", under_20)
print("not under_20:", not under_20)


if True:
    print("True입니다...!")
    print("정말 True입니다...!")


if True:
    print("정답!")   # tab : 탭  / shift + tab : 탭 제거


data = input('숫자를 입력해 주세요> ')
data = int(data)
x = int(data)
if x > 0:
    print("양수입니다.")
elif x < 0:
    print("음수입니다.")
elif x == 0:
    print("0입니다.")


number = input('숫자를 입력해 주세요>')
number = int(number)    # 문자열 => 숫자  (형변환, 캐스팅)
if number == 0:
    print('0 이네요!')
elif number > 0:
    print('양수네요!')
elif number < 0:
    print('음수네요!')
else:
    print('처리 불가')