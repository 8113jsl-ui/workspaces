# 배열의 원소만큼 추가하기

def solution(arr):
    answer = []
    for i in arr:
        for n in range(i):
            answer.append(i)
    return answer