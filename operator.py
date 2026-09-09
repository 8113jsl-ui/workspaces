# 연산자
# 원주율 3.14, 반지름 10인 원의 둘레와 넓이 구하기

# 1. 데이터 => 반지름, 원주율, 지름
radius = 10
pi = 3.14


# 2. 계산식을 이용하여 둘레와 넓이를 구한다.

circumference = radius * 2 * pi
area = radius * radius * pi

# 3. 구한 둘레와 넓이를 형식에 맞도록 출력한다.

print("원의 둘레:", circumference)
print("원의 넓이:", area)

print("원의 둘레: " + str(circumference))
print("원의 넓이: " + str(area))