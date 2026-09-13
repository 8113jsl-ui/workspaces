# 마지막 두 원소

def solution(num_list):
    answer = []
    f = len(num_list) - 1
    add = num_list[f] - num_list[f-1]
    for i in num_list:
        answer.append(i)
    if num_list[f] > num_list[f-1]:
        answer.append(add)
    else:
        answer.append(2*num_list[f])
    return answer


