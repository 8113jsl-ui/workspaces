# 원하는 문자열 찾기

def solution(myString, pat):
    answer = 0
    if pat.lower() in myString.lower():
        answer = 1
    else:
        answer = 0
    return answer