# 짝수, 홀수

# 1. 끝자리로 구분하기
number = input('숫자를 입력하세요> ')

lastchr = number[-1]  # 문자열의 마지막 글자
lastchr = int(lastchr)


if (lastchr == 0) or (lastchr == 2) or (lastchr == 4) or (lastchr == 6) or (lastchr == 8):
    print('입력한 숫자 {}는 짝수입니다.'.format(number))
else:
    print('입력한 숫자 {}는 홀수입니다.'.format(number)
    )