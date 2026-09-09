# break.py
# 변수를 선언합니다.
i = 0

# 무한 반복합니다.
while True:
    # 몇 번째 반복인지 출력합니다.
        print("{}번째 반복입니다.".format(i))
        i = i + 1    
        input_text = input("> 종료하시겠습니까?(y/n): ")
        if input_text in ["y", "Y"]:
           print("반복을 종료합니다.")
           # 반복을 종료합니다.
           break