# 모듈 만들기

# main.py 파일
import test_module as test

radius = test.number_input() # number_input() 함수가 이미 정의되어 있음
print(test.get_circumference(radius)) # get_circumference() 함수가 이미 정의되어 있음
print(test.get_circle_area(radius)) # get_circle_area() 함수가 이미 정의되어 있음

# 실제 실행하는 코드 : main.py
    # 실행화면 (사용자가 사용하는 화면)


# __name__ : 내부 변수 (시스템 변수)
__name__ == "__main__"

# 프로그램의 시작점 : 엔트리 포인트 = 엔드포인트 = 메인(main)

# 모든 시작점은, "__main__" 함수