import datetime   
# datatime 라이브러리 불러오기
# 시스템으로부터 시간을 받아오기 위해

now = datetime.datetime.now()
print(now)

# datetime의 field (열)을 잘라올 수 있다
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초") 
print(now.microsecond, "마이크로초")


print(format(now, "%Y"))
print(format(now, "%y"))
print(format(now, "%m"))

print('{}년 {}월 {}일'.format(now.year, now.month, now.day))


