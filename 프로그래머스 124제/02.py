# 특정한 문자를 대문자로 바꾸기

def solution(my_string, alp):
    answer = ''
    for letter in my_string:
        if letter == alp:
            letter = alp.upper()
        answer += letter
    return answer