# 모듈을 읽어 들입니다.
from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽습니다.
target = request.urlopen("https://google.com")
output = target.read()# 출력합니다.
print(output)


# 실행결과 : google.com 페이지 소스

# 이 결과를 원하는 형태로 커스텀 -> 나에게 맞는 용도로 사용