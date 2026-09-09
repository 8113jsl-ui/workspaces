list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]     # 인덱스 3, 4, 5 삭제 -> 3, 4, 5 삭제
print(list_b)

del list_b[3:]     # 인덱스 3 이후 삭제
print(list_b)

del list_b[:3]     # 인덱스 0부터 2까지 삭제
print(list_b)


# 슬라이싱은 마지막 위치에 '단계'라는 부분을 추가할 수 있습니다. 단계를 사용하면 지정한 숫자만큼 인덱스를 건너뛰며 요소를 가져옵니다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:5:2])       # [1, 2, 3, 4, 5] -> 2 간격으로 -> [1, 3, 5]
print(numbers[0:5:3])

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[::-1])   
print(numbers[::-2])
# 시작/끝 인덱스는 자동으로 "전부"가 지정됩니다