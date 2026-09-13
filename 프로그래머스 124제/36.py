# 부분 문자열인지 확인하기

def solution(my_string, target):
    answer = 0
    if target in my_string:
        answer = 1
    else:
        answer = 0
    return answer
