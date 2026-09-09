array = [273, 32, 103, "문자열", True, False]
print(array)


data = [1, 2, 3, 4]
hi = ["안", "녕", "하", "세", "요"]
mixed = [273, 32, 103, "문자열", True, False]

# element : 리스트 각각의 요소

# 리스트 data에 첫번째 요소의 값을 list1이라는 변수에 저장하세요.
list1 = data[0]

# list1에 저장된 값을 출력하고 숫자라면 해당 값에 2를 더하시오.
print(list1)

list1 = list1 + 2
print(list1)


# data 리스트의 3번째 요소와 5번째 요소의 값을 합하여 list2 변수에 저장 후 출력하시오.
data = [1,2,3,4,5,6,7,8,9,10,"문자열"]
list2 = data[2] + data[4]

print('{} + {} = {}'.format(data[2],data[4],list2))



list3 = data[1:3]       # 슬라이싱 [a:b] : a ~ b-1까지
print(list3)
print(data[1],data[2])

print(data[-1],data[-10])   # [-0] : [0]과 동일


print(data[10][1])      # 리스트.[][] : 첫번째 [] 인덱스 값 = a -> a도 하나의 연속된 값(값이 하나하나 저장되어 있음 ex) "문자열" -> 문/자/열 -> a에서 두번째 [] 인덱스 위치의 값 = b
                        # 리스트 = ["이재서", "김재서"] -> 리스트[1][2] = 김/재/서 의 "서"
                        # 즉 [][] : [행][열]   ---->   표 Table



list_a = [273, 32, 103, "문자열", True, False]
print(list_a[3])
print(list_a[3][0])


list_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]      # 리스트 안에 리스트 3개가 있다
print(list_b[1])
print(list_b[1][1])
listlist = list_b[0][2]
print(listlist)

# list_b의 3과 8을 더해 11이 출력되게 해보시오.
listlist2 = list_b[2][1]

print(listlist + listlist2)


# 표로 시각화
#       0    1    2
# 0     1    2    3
# 1     4    5    6
# 2     7    8    9




