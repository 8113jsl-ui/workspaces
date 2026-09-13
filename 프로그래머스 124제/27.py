# 문자열 앞의 n글자

def solution(my_string, n):
    answer = ''
    for i in range(n):
        answer += my_string[i]
    return answer