# lambda 함수
# lambda 매개변수: 리턴값 (lambda y: x)

list_a = [1,2,3,4,5]



# 더 간단한 방법 : 함수 정의 없이, lambda 식 -> 매개변수로 넣기

# map 함수
output_a = map(lambda x: x*x, list_a)
print("제곱:", list(output_a))

# filter 함수
output_b = filter(lambda x: x<3, list_a)
print("3 이하 숫자:", list(output_b))