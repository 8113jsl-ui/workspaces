# [4번 문제]
# 입력받은 점수를 “ABCDF”로 평가하는 프로그램을 작성하시오. (조건: 90점 이상 A , 80점 이상 B, 70점 이상 C, 60점 이상 D,60점 미만 F)

# 1. 점수 1개를 입력받음 - int(input())
# 2. 조건문 - 점수 구간별로 조건 나눔
# 3. print(등급)

score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")
