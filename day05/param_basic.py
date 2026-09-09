def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 3)



def print_customized(message, i):
    for n in range(i):
        print(message)

print_customized("초아뭉이", 10)




# [오류 1] 매개변수를 빠뜨리고 함수를 호출하는 경우 -> TypeError
print_customized("초아뭉이")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: print_customized() missing 1 required positional argument: 'i'



# [오류 2] 매개변수를 더 많이 넣은 경우
print_customized("초아뭉이"4,4)
[오류]
# Traceback (most recent call last):
#   File "test5_02.py", line 6, in <module>
#     print_n_times("안녕하세요", 10, 20)
# TypeError: print_n_times() takes 2 positional arguments but 3 were given