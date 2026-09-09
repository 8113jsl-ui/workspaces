# test_module.py 파일
PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):  
  return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius


# 객체지향 프로그래밍에서는, 단위별로 파일 분리
# 스레드 : 시스템에서 한번 운영되는 단위
# 컴포넌트를 분리해서 -> 재사용성 있게 -> 프로그램 설계!

# main.py, test_module.py -> 역할에 따라 파일 분리
    # 사용자는 입력값만 넣으면 됨




# import를 이용해서,
# 다른 파일의 코드를 "묶음" 단위로 가져와 쓸 수 있다 = 재사용성



# 모듈
# 함수, 변수, 상수를 하나의 파일에 묶음으로 저장한 것



# 패키지
# 여러 모듈을 묶어서 관리하는 것

# 루트에 패키지를 저장함
# 각 패키지에 모듈들이 있고 -> 이 모듈들을 사용할 때 -> 루트에서 "매뉴얼"을 배포해줌

