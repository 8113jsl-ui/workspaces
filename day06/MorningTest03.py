##### 기본 개념 문제 #####
# 1. 리스트로 평균 구하기
scores = [85, 92, 78, 90, 88]
total = 0

for i in range(len(scores)):
    total += scores[i]
    
avrg = total/len(scores)

print(total)
print(avrg)


# 2. 딕셔너리로 정보 조회하기
student = {"이름": "김클라라", "나이": 25, "전공": "컴퓨터공학"}

print("이름", ":", student["이름"])
print("나이", ":", student["나이"])

# 3. 짝수/홀수 분류하기
even_list = []
odd_list = []

for i in range(1,21):
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
    
    
print("짝수:", even_list)
print("홀수:", odd_list)
        


# 4. 사칙연산 함수 만들기
def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)
    
def divide(a, b):
    print(a / b)

add(10, 2)
subtract(30, 50)
multiply(3, 5)
divide(100, 25)

# 5. 구구단 출력하기

while True:
    for number in range(2,10):
        for i in range(1,10):
            print(f'{number} x {i} = {number * i}')
    break




##### 실무 응용 문제 #####

# 1. 학생 성적 관리 시스템
students = [{"이름": "김클라라", "점수": 90},
            {"이름": "이개발", "점수": 75}]


def add_student(name, score):
    new = {}
    new["이름"] = name
    new["점수"] = score
    students.append(new)


def get_average():
    total = 0

    for i in range(len(students)):
        total += students[i]["점수"]

    avrg = total / len(students)

    print(avrg)


def get_top_students():
    total = 0

    for i in range(len(students)):
        total += students[i]["점수"]

    avrg = total / len(students)

    for i in range(len(students)):
        if students[i]["점수"] >= avrg:
            print(students[i]["이름"])


get_average()
get_top_students()



# 2. 온라인 쇼핑몰 장바구니 계산기
cart = [      {"상품명": "키보드", "가격": 50000, "수량": 1},      
        {"상품명": "마우스", "가격": 20000, "수량": 2},  ]


def calculate_total(cart):
    total = 0
    for i in range(len(cart)):
        total += (cart[i]["가격"] * cart[i]["수량"])
    if total >= 50000:
        total = total * 0.9
    print(total)
    

calculate_total(cart)



# 3. 회원 등급 필터링 시스템
client = [
    {"고객명": "김철수", "구매금액": 1200000},
    {"고객명": "이영희", "구매금액": 700000},
    {"고객명": "박민수", "구매금액": 300000},
    {"고객명": "최지우", "구매금액": 1500000}
]


def get_grade(amount):
    if amount >= 1000000:
        return "VIP"
    elif amount >= 500000:
        return "일반"
    else:
        return "신규"


vip_list = []

for i in range(len(client)):
    client[i]["등급"] = get_grade(client[i]["구매금액"])

    if client[i]["등급"] == "VIP":
        vip_list.append(client[i]["고객명"])


print(client)
print(vip_list)

# 4. 텍스트 단어 빈도수 분석기
text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"

word = text.split()  # 결과 : 리스트 []

word_count = {}

for i in range(len(word)):
    if word[i] in word_count:
        word_count[word[i]] += 1    # word_count 딕셔너리에 있는 단어 -> 개수 1개 추가
    else:
        word_count[word[i]] = 1     # word_count에 없던 단어 -> 1로 시작
    

print(word_count)


# 5. 간단한 To-Do 리스트 관리 프로그램
to_do_list = []


def add_task():
    to_do_list_input = input("할 일을 입력하세요: ")

    current = {}
    current["할일"] = to_do_list_input
    current["완료"] = False

    to_do_list.append(current)


def delete_task():
    to_do_list_input = input("삭제할 일을 입력하세요: ")

    for i in range(len(to_do_list)):
        if to_do_list[i]["할일"] == to_do_list_input:
            to_do_list.remove(to_do_list[i])
            break


def show_task():
    print(to_do_list)


while True:
    menu_input = input("메뉴를 입력하세요 (추가/삭제/조회/종료): ")

    if menu_input == "추가":
        add_task()

    elif menu_input == "삭제":
        delete_task()

    elif menu_input == "조회":
        show_task()

    elif menu_input == "종료":
        break
    else:
        continue