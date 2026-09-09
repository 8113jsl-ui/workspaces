# 사용자 함수 호출 (투수) -> 함수 매개변수 (포수)

def get_input(prompt, value):
    try:  # try 예외처리 구문    
        return input(prompt)
    except EOFError: # EOFError는 input() 함수가 더 이상 읽을 데이터가 없는 파일이나 입력의 끝(EOF, End of File) 상태에 도달했을 때 발생
        print(f"입력처리 불가 -> {value} 기본 값으로 진행합니다.")
        return value

# ===========================================================================================
# [응용 실무 문제]
# 1. 학생 성적 관리 시스템 — [딕셔너리 + 리스트 + 함수 + 반복문]
# 시나리오: 여러 학생의 정보를 리스트 안의 딕셔너리로 관리합니다.
# python
# 요구사항:
# 학생을 추가하는 함수 add_student(name, score)
# 전체 평균을 구하는 함수 get_average()
# 평균 이상인 학생만 출력하는 함수 get_top_students()
# ===========================================================================================

# ↑ "인터페이스" : 함수 정의, 프로젝트 내용 등을 정리한 상황판
students = [      {"이름": "김클라라", "점수": 90},      {"이름": "이개발", "점수": 75},  ]

def add_student(name, score):
    students.append({"이름":name, "점수":score})

def get_average():
    if not students:
        return 0
    
    total = 0
    for student in students:
        total += student["점수"]    # 전체 학생의 점수 합계

    averageValue = total / len(students)
    return averageValue


# def get_average():
#     if not students:
#         return 0
    
#     total = 0
#     averageValue = 0.0  # 변수 정의를 먼저 하는 게 -> 정석!
#     for student in students:
#         total += student["점수"]    # 전체 학생의 점수 합계

#     averageValue = total / len(students)
#     return averageValue



def get_top_students(): # 평균 점수 이상 학생들만 새 리스트에 반환하는 함수
    avg = get_average() # 함수에서 함수 호출 가능(Call Chain: 호출하면 실행)
                        # get_average() == 점수 평균
    return [s for s in students if s["점수"] >= avg ]
            # s : students 리스트 요소 ({"이름": "김클라라", "점수": 90}, {"이름": "이개발", "점수": 75})
            

add_student("서유미",80)
print(f"평균점수 : {get_average():.1f}") # .1f : 소수점 첫째자리까지 float 처리
print(f"평균 이상 우수 학생 : {get_top_students()}")




# 딕셔너리 : 1개의 품목의 정보를 담는 그릇 (계란)
# 리스트 : 여러 품목들을 담는 그릇 (계란판)

# ===========================================================================================
# 2. 온라인 쇼핑몰 장바구니 계산기 — [리스트/딕셔너리 + 함수 + 제어문]
# 시나리오: 장바구니에 담긴 상품(이름, 가격, 수량)의 총 결제금액을 계산합니다.
# python
#   cart = [      {"상품명": "키보드", "가격": 50000, "수량": 1},      {"상품명": "마우스", "가격": 20000, "수량": 2},  ]
# ​
# 요구사항:
# 총 금액을 계산하는 함수 calculate_total(cart)
# 총 금액이 50,000원 이상이면 10% 할인을 적용하는 조건문 추가
# 최종 결제 금액 출력
# 💡 비유: 실제 쇼핑몰 백엔드의 "장바구니 로직"이 바로 이런 구조예요. 지금 짜는 이 함수가 나중에 실제 서비스의 핵심 로직이 될 수 있습니다.
# ===========================================================================================
cart =[      {"상품명": "키보드", "가격": 50000, "수량": 1},     
          {"상품명": "마우스", "가격": 20000, "수량": 2},  ]

print("=====응용문제 2번 장바구니 구현=====")

def calculate_total(cart):
    # 딕셔너리 리스트를 받아서 할인 전 총금액 계산하기
    total = 0  # 할인 전 총금액 저장 변수
    for item in cart:
        total += item["가격"] * item["수량"]
    return total

def apply_discount(total):
    if total >= 50000:
        discount = total * 0.1
        return total - discount   # 조건(5만원 이상) 만족하면 -> discount 금액만큼 차감해서 total 값 반환
    return total  # 조건 만족하지 않으면(5만원 미만) -> 그냥 total 반환

print("cart 실행")
subtotal = calculate_total(cart)
final_price = apply_discount(subtotal)

print(f'할인 전 금액 : {subtotal: ,}원')
print(f'최종 결제 금액 : {final_price: ,.0f}')


        
# ===========================================================================================
# 3. 회원 등급 필터링 시스템 — [제어문 + 반복문 + 함수]
# 시나리오: 회원 목록에서 나이/구매금액 조건에 맞는 회원만 뽑아 등급을 부여합니다.
# 요구사항:
# 구매금액이 100만원 이상이면 "VIP", 50만원 이상이면 "일반", 그 미만이면 "신규"로 등급을 매기는 함수 get_grade(amount)
# 회원 리스트를 순회하며 각 회원의 등급을 딕셔너리에 추가
# "VIP" 등급 회원만 따로 리스트로 출력
# 🎯 포인트:  실무의 "고객 세그멘테이션(고객 분류)" 로직 미니 버전입니다. 마케팅/CRM 도메인 프로젝트로 확장할 수 있습니다.
# ===========================================================================================
print("=====회원 등급 VIP 필터링=====")
members = [
    {"이름": "이재서", "구매금액": 1000000, "등급": "VIP"},
    {"이름": "제나", "구매금액": 500000, "등급": "일반"},
    {"이름": "리브", "구매금액": 2000000, "등급": "VIP"},
    {"이름": "원이", "구매금액": 300000, "등급": "신규"}
]


# 구매금액에 따른 등급 문자열 반환 함수
def get_grade(amount):
    if amount >= 1000000:
        return "VIP"
    elif amount >= 500000:
        return "일반"
    else:
        return "신규"
    
# 회원 리스트를 순회하면서, 각 딕셔너리의 "등급"key 새로 추가
for member in members:
    member["등급"] = get_grade(member["구매금액"])

# 회원 목록 출력
print(f'등급이 매겨진 회원 목록 : {members}')


# 등급이 VIP인 멤버만 출력 (리스트 컴프리헨션)
vip_members = [v for v in members if v["등급"] == "VIP"]
print(f'VIP 회원 리스트 : {vip_members}')









# ===========================================================================================
# 4. 텍스트 단어 빈도수 분석기 — [딕셔너리 + 반복문 + 함수]
# 시나리오: 긴 문장(예: 리뷰 텍스트)에서 각 단어가 몇 번 등장하는지 세는 프로그램을 만듭니다.
# python
#   text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"
# ​
# 요구사항:
# 공백 기준으로 단어를 나누고(split()), 딕셔너리에 {단어: 등장횟수} 형태로 저장
# 가장 많이 등장한 단어 TOP 3을 출력
# 💡 연결고리: 이 문제는 임베딩(문장을 숫자로 바꾸는 것)이나 RAG(문서 검색 기반 AI 응답)의 아주 첫걸음이에요. "컴퓨터가 텍스트를 이해하려면 결국 숫자로 세는 것부터 시작한다"는 감각을 여기서 미리 잡아줄 수 있습니다.
# # ===========================================================================================


# [Pseudo Code]
# 1단계 : text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"를 공백 기준을 split
# 2단계 : 공백 단위 분리된 리스트 -> 변수에 저장
# 3단계 : 변수에 저장된 리스트 -> 각 요소가 등장할 때마다 -> 개수 +1 -> 변수에 저장
# 4단계 : 변수에 저장된 count를 비교해서 Top 3 출력 
print("=====텍스트 단어 빈도수 계산하기=====")

text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"

#1 문장을 쪼갠 후, {단어: 개수} 구성하여 반환하는 함수
def count_word(sentence):
    words = sentence.split()  # split() -> 공백을 기준으로 문자열을 리스트로 반환 / split(구분자) -> 구분자 기준으로 문자열 리스트로 반환
    counts = {}
    for word in words:
        # dict.get(key, 기본값) : key가 존재한다면 -> 해당 값을 리턴 / key가 없으면 -> 0을 리턴
        counts[word] = counts.get(word,0) + 1
        return counts
    
word_count = count_word(text)
print(word_count)


#2 정렬 : 가장 많이 등장하는 단어 Top3 => 내림차순(Descending)

# sorted() : 원본 그대로 (비파괴적) -----> 여기선 이게 적합함!
# sort() : 원본 변경 (파괴적)

sorted_words = sorted(word_count.items(), key=lambda x:x[1], reverse=True)

#3 출력 (텍스트 -> 숫자(정수)로 바꾸는 과정 = 임베딩)
top3 = sorted_words[:3]
print(f'가장 많이 등장한 단어 Top3 : {top3}')


# 청킹(chunking) = split

# 임베딩 : 문자열 -> 숫자로 만듦 (유사도에서 빈도 측정이 매우 중요)
# RAG : 임베딩 원리, 방식
# Retrieval System







# ============================================================================
# [응용 문제 5] 간단한 To-Do 리스트 관리 프로그램
# - 시나리오: 사용자가 메뉴를 선택해 할 일을 추가/삭제/조회하는 콘솔 프로그램입니다.
# - 요구사항:
#     1. `while` 반복문으로 프로그램이 계속 실행되도록 메뉴(추가/삭제/조회/종료)를 반복 출력
#     2. 각 기능을 함수로 분리: `add_task()`, `delete_task()`, `show_tasks()`
#     3. 할 일 목록은 리스트에 저장, 완료 여부는 딕셔너리(`{"할일": "장보기", "완료": False}`)로 관리
# ============================================================================
print("간단한 To-Do 리스트 관리 프로그램")

tasks = []   # {"할일":str,"완료":bool}

def add_task(task):
    tasks.append({"할일":task,"완료":False})

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"'{removed['할일']}'삭제완료")
    else: 
        print("잘못된 번호입니다.")

def complete_task(index):
    if 0<= index <len(tasks):
        tasks[index]['완료'] = True

def show_tasks():
    if not tasks:
        print("할일 목록이 비어 있습니다.")
        return 
    for i,task in enumerate(tasks):
        status = "완료" if task["완료"] else "미완료"
        print(f"{i}.{task['할일']} [{status}]")

def todo_run():
    while True:

        print("\n[메뉴] 1. 추가 2.삭제 3.완료처리 4.전체조회 5.종료")
        choice = get_input("메뉴 번호 선택 > ", "5")

        if choice == "1":
            name =get_input("할 일을 입력하세요: " , "예: 할일")
            add_task(name)
        elif choice == "2":
            idx = get_input("삭제할 번호: " , "0")
            delete_task(int(idx))

        elif choice == "3":
            idx = get_input("완료 처리 번호 입력> " , "0")
            complete_task(int(idx))

        elif choice == "4": 
            show_tasks()

        elif choice == 5:
            print("Todo 프로그램 종료")
            break
        else:
            print("메뉴 번호는 1-5 번 까지 입니다. ")

todo_run()