# 주사위 게임 1

def solution(a, b):
    answer = 0
    a in [1,2,3,4,5,6]
    b in [1,2,3,4,5,6]
    if (a%2 != 0) and (b%2 != 0):
        answer = a**2 + b**2
    elif (a%2 != 0) or (b%2 != 0):
        answer = 2*(a + b)
    else:
        answer = abs(a - b)
    return answer