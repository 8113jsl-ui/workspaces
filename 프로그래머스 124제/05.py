# 조건에 맞게 수열 변환하기 3

def solution(arr, k):
    answer = []
    if k%2 != 0:
        for i in arr:
            answer.append(i * k)
    else:
        for i in arr:
            answer.append(i + k)
    
    return answer