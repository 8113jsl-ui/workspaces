# [7번 문제]
# 아래의 메뉴에서 선택한 메뉴를 알려주는 프로그램을 작성하시오

# 1. 메뉴 출력



print('1. 삽입')
print('2. 수정')
print('3. 삭제')

# 2. 사용자로부터 메뉴 번호를 입력받기
user_choice = int(input('숫자를 입력해주세요: '))

# 선택한 번호에 따라 결과 출력
if user_choice == 1:
    print('삽입을 선택하셨습니다.')
elif user_choice == 2:
    print('수정을 선택하셨습니다.')
elif user_choice == 3:
    print('삭제을 선택하셨습니다.')
else:
    print('잘못된 입력입니다!')