# 1-3. 주의: range()의 매개변수는 반드시 정수

n = 10
a = range(0, n / 2)

# TypeError: 'float' object cannot be interpreted as an integer

a = range(0, int(n / 2))  
# 실수를 정수로 변환
print(list(a))
# [0, 1, 2, 3, 4]

a = range(0, n // 2)        
# 정수 나누기 연산자(권장)

print(list(a))              
# [0, 1, 2, 3, 4]
