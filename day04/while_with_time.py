import time   
# 예: 1557241486.6654928 = (1970-01-01부터) 몇 초가 지났는가?


print(time.time())
# while_with_time.py
# 시간과 관련된 기능을 가져옵니다.
import time

# 변수를 선언합니다.
number = 0

# 5초 동안 반복합니다.
target_tick = time.time() + 5                               # 5초 동안 숫자 출력

# 5초 동안 while 문을 실행한다! (end 조건 = 5초)
while time.time() < target_tick:
    number += 1
    # 출력합니다.
    print("5초 동안{}번 반복했습니다.".format(number))
    # 예: 5초 동안 14223967번 반복했습니다.


# while은 반드시 end 조건 필요! (없으면, 무한루프)