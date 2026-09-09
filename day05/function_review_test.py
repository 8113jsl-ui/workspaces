# 마무리

# 확인문제

# 1. 다음과 같이 방정식을 파이썬 함수로 만들어 보세요.
# 예: f(x) = x

def print_x(value):
    print(value)

print_x("집 가고 싶다")



# ① f(x) = 2x + 1

def print1(value):
    print(2*value + 1)

print1(10)



# ② f(x) = x² + 2x + 1
def print2(value):
    print(value**2 + 2*value + 1)

print2(5)




# 2. 다음 빈칸을 채워 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수를 만들어 보세요.

def mul(*values):
    result = 1
    for v in values:
        result *= v
    return result

print(mul(5,7,9,10))



# 3. 다음 중 오류가 발생하는 코드를 고르세요.

# 정답 : ① def function(*values, valueA, valueB):    passfunction(1, 2, 3, 4, 5)    passfunction(1, 2, 3, 4, 5)

def function(*values, valueA, valueB):    
    pass

function(1, 2, 3, 4, 5)

# 오류 내용
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: function() missing 2 required keyword-only arguments: 'valueA' and 'valueB'