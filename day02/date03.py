# month로 계절을 구분하기

import datetime

date = datetime.datetime.now()

if 3 <= date.month <= 5:
    print(format('{}월은 봄입니다').format(date.month))
elif 6 <= date.month <= 8:
    print(format('{}월은 여름입니다').format(date.month))
elif 9 <= date.month <= 11:
    print(format('{}월은 가을입니다').format(date.month))
elif date.month == 12 or 1 <= date.month <= 2:
    print(format('{}월은 겨울입니다').format(date.month))