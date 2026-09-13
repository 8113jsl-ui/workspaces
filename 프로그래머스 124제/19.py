# 두 수의 연산값 비교하기

def solution(a, b):
    answer = 0
    link = int(str(a) + str(b))
    if link >= 2*a*b:
        answer = link
    else:
        answer = 2*a*b
    return answer