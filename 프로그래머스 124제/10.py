# 원소들의 곱과 합

def solution(num_list):
    answer = 0
    total = 0
    multiply = 1
    for i in num_list:
        multiply *= i
        total += i
        if multiply < total**2:
            answer = 1
        else:
            answer = 0
        
    return answer