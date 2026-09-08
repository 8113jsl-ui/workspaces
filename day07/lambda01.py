# 람다 lambda 
# : 매개변수로 함수를 전달하기 위해 함수 구문을 작성하는 것이 번거롭고, 코드 낭비라 생각이 들 때 함수를 간단하고 쉽게 선언하는 방법
#   - 화살표 표기법 : ( ) -> { }
#   - 특징 : 1회용 함수를 만들 때 사용한다



# 콜백 함수 (Callback) : 함수를 호출하는 함수
# 이를 효율적으로 작성하기 위해 파이썬 -> lambda 사용
# AI 업무자동화의 기본 원리 = 콜백 함수

def call_10_times(func):  # 매개변수 = 함수
    for i in range(10):
        func()


def print_hello():
    print("Hello!")
    
call_10_times(print_hello)
# 괄호 안이 print_hello() 가 아닌 이유 : print_hello() 함수가 call_10_times()의 파라미터가 된다. 
# call_10_times 함수에 print_hello()의 주소값을 전달한다.
# 따라서 call_10_times(print_hello)



# lambda 함수
# filter() / map() 함수
# filter(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴값이 True
# map(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수 
# 함수를 매개변수로 사용하는 대표적인 표준 함수

