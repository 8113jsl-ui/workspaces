list_a = [1,2,3,4,5,6,7,8,9]

# for, range() 함수
for i in range(10):
    print(i)


for i in range(10,0,-1):            # range(시작,끝,간격) : 끝값은 포함되지 않는다!
    print(i)                        # 즉, range(10,0,-2) -> 10, 8, 6, 4, 2
                                    # range(시작값,끝값,증가값)
                                            # 시작값, 끝값, 증가값 -> 인자값
                                    # 방향에 상관없이, "끝값은 항상 포함되지 않는다!"

for i in range(10,-1,-1):
    print(i)

for i in range(10,0,-3):
    print(i)


# reversed() 함수
numbers = [10,20,30,40,50]             # 포인터 : 주소값을 저장하는 변수  -> numbers변수에는, [10,20,30,40,50] 요소에 대한 주소값이 저장되어 있다.
for number in numbers:
    print(number)

for number in reversed(numbers):        # reversed(리스트, 문자열)
    print(number)

for number in numbers[::-1]:            # 슬라이싱 : [시작:끝:간격]   /   [::] : 처음부터 끝까지
    print(number)