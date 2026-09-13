# 배열의 원소 삭제하기

def solution(arr, delete_list):
    answer = []
    return [x for x in arr if x not in delete_list]