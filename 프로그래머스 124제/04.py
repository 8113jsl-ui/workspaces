# 홀짝에 따라 다른 값 반환하기

def solution(n):
    answer = 0
    if n%2 == 0:
        for i in range(2, n+1, 2):
            answer += i**2
    else:
        for i in range(1, n+1, 2):
            answer += i
            
    return answer