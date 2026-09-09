# 짝수, 홀수

# 2. in 연산자
number = input('숫자를 입력하세요> ')

lastchr = number[-1]  # 문자열의 마지막 글자
lastchr = int(lastchr)

if lastchr in [0,2,4,6,8]:
    print('입력한 숫자 {}는 짝수입니다.'.format(number))
else:
    print('입력한 숫자 {}는 홀수입니다.'.format(number))