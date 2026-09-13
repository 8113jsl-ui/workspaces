# 첫번째로 나오는 음수

def solution(num_list):
    answer = 0
    5 <= len(num_list) <= 100
    for i in range(len(num_list)):
        -10 <= num_list[i] <= 100
        if num_list[i] < 0:
            answer = i
            break
        else:
            answer = -1
    return answer