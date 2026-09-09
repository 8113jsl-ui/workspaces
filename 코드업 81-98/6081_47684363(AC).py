hexa_input = input()

for i in range(1, 16):  # 16진수 구구단은 F(15)단까지만 출력하므로 16을 제외해야 합니다.
    print(f"{'%X'%int(hexa_input, 16)}*{'%X'%i}={'%X'%(int(hexa_input, 16) * i)}")
