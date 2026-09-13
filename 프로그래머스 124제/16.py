# 문자열의 뒤의 n글자

def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        answer = my_string[-1:-1-n:-1]
        answer = answer[::-1]
            
    return answer