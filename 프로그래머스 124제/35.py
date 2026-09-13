# 더 크게 합치기

def solution(a, b):
    answer = 0
    link1 = int(str(a)+str(b))
    link2 = int(str(b)+str(a))
    if link1 >= link2:
        answer = link1
    else:
        answer = link2
    return answer