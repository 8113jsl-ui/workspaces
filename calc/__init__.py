# calc 라는 디렉토리 -> 모듈로 인식시키기 위해 -> __init__.py 파일 생성

# import calc.basic, calc.advanced  # 패키지로 호출하기!


# __all__ : 내부변수
# __all__ = [
#     "basic"
# ]


# basic, advanced이든 상관없이, 함수를 불러오고 싶을 때
from calc.basic import *
from calc.advanced import *
