omok = []       

# 각 바둑판 좌표를 0으로 표현
for i in range(20):
    omok.append([])  # 하위 리스트 생성
    for j in range(20): 
        omok[i].append(0)  # 각 하위 리스트마다, 19개의 "0" 생성

n = int(input())
for i in range(n):
    x, y = input().split()  # 숫자 2개를 공백을 두고 입력 & 저장
    omok[int(x)][int(y)] = 1  # 각 하위 리스트의 19개의 "0"에, "1" 할당

for i in range(1, 20):
    for j in range(1, 20):
        print(omok[i][j], end=' ')  # 19 * 19 좌표 출력
    print()
