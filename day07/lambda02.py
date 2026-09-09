# lambda 함수
# lambda 매개변수: 리턴값 (lambda y: x)


# 함수 선언
power = lambda x: x*x
under_3 = lambda x: x<3


list_a = [1,2,3,4,5]


# map 함수
output_a = map(power, list_a)
print("제곱:", list(output_a))

# filter 함수
output_b = filter(under_3, list_a)
print("3 이하 숫자:", list(output_b))