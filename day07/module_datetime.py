# 모듈을 읽어 들입니다.
import datetime

now = datetime.datetime.now()

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")  # strftime : 원하는 포맷으로 시간 출력 (영어만 가능)
output_b = "{}년{}월{}일{}시{}분{}초".format(    now.year,    now.month,    now.day,    now.hour,    now.minute,    now.second)

output_c = now.strftime("%Y{} %m{}%d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)


# 특정 시간 이후의 시간 구하기
print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(    weeks=1,    days=1,    hours=1,    minutes=1,    seconds=1)
print(after.strftime("%Y{} %m{}%d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()# 특정 시간 요소 교체하기
print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{}%d{} %H{} %M{} %S{}").format(*"년월일시분초"))