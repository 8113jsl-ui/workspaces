# 튜플은 함수의 return에 많이 사용된다
# 함수의 리턴에 튜플을 사용하면 여러 값을 한번에 전달할 수 있기 때문이다

# test 함수 정의
def test3():
    return 100

def test():
    return 10,20

def test1():
    return (10,20)

def test2():
    value = 30,24
    return value


print(test()) # 결과 : 튜플
print(test1()) # 결과 : 튜플
print(test2()) # 결과 : 튜플
print(test3())

a,b = test1()
print(a) # test1() return의 첫번째 값
print(b) # test1() return의 두번째 값

print()

# enumerate
print(" 실무 예제 for     enumerate()")

for i, value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소: {}입니다".format(i, value))
