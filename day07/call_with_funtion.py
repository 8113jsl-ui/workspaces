# 함수를 선언한다.

def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

# map() 함수 
output_a = map(power, list_input_a)
print("output_a:", output_a)
# 결과 = output_a: <map object at 0x000002397174ACB0>
# 0x000002397174ACB0 = 주소값

print("output_a:", list(output_a))



# filter() 함수
output_b = filter(under_3, list_input_a)  
# filter함수가 -> under_3가 True 값만 -> 리스트로 뽑아냄

print("output_b:", output_b)
print("output_b:", list(output_b))


# 제너레이터 - 중요!
# output_a: <map object at 0x000002146D3EBA90>
# output_b: <filter object at 0x000002146D3EB8B0>




# lambda 함수
# lambda 매개변수: 리턴값