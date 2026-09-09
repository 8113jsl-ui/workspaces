# 1. extend() : 리스트가 변함 (파괴적)
list_a = [1, 2, 3]
list_a.extend([4, 5, 6])
print(list_a)



# 2. + 연산자로 처리 시 : 리스트 변하지 않음 (비파괴적)
list_a = [1, 2, 3]
list_b = [4, 5, 6]
# 리스트 연결 연산자로 연결하기
print(list_a + list_b)
print(list_a)   
# list_a에는 어떠한 변화도 없습니다 (비파괴적 처리)
print(list_b)   
# list_b에도 어떠한 변화도 없습니다 (비파괴적 처리)