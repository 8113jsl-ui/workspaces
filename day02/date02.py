# 현재 시간(now)을 시스템으로부터 가져와서 오전, 오후 판단하는 프로그램
# 오전, 오후의 기준은 12시로 정한다

import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("오전", now.hour, "시입니다")
elif now.hour == 12:
    print("정오입니다")
elif now.hour > 12:
    print("오후", now.hour, "시입니다")
elif now.hour == 24:
    print("자정입니다")



# 소용우님 - format 버전
a = datetime.datetime.now()
if a.hour < 12:
    print("현재 시간은 {}시로 오전입니다.".format(a.hour))
elif a.hour == 12:
    print("현재 시간은 {}시로 정오입니다.".format(a.hour))
else:
    print("현재 시간은 {}시로 오후입니다.".format(a.hour))