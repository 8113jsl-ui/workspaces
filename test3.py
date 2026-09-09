from calc import *    # * : 아스트리스 (al1 의미)

print(basic.add(10,20))
# print(advanced.multiply(5,9))
# NameError: name 'advanced' is not defined
# __init__.py에서, __all__에 "basic"만 있음
# 따라서 "advanced"는 실행되지 않음