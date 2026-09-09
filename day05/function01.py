# 기초 1. len() — 글자 수 세기
# 설명: 목걸이에 구슬이 몇 개 꿰어져 있는지 세는 것과 같아요. 공백도 구슬 1개로 셉니다.
# 문법: len(문자열)

name = "AI개발자"
print(len(name))



# 기초 2. .upper() / .lower() — 대소문자 바꾸기
word = "Hello Python"
print(word.upper())
print(len(word.upper()))
print()
print(word.lower())


#### 라이브러리 : 내장 함수

# function chaining : 여러 함수를 연결해서 사용 = 람다 방식
# 최종 함수 / 터미널 함수 : 가장 바깥쪽
# len(word.upper()) -> 최종 함수 : len()




# 기초 3. .strip() 양쪽 공백/문자 제거

user_input = "   챗봇에게 질문할게요   "
# 사용자는 우리가 원하는 형태로 입력하지 않는다
# therefore, 공백 제거 필수! 

print("1", len(user_input))
user_input = user_input.strip()
print("2", len(user_input))


print(user_input.strip("요"))

# 응용 1. .split() — 구분자로 잘라서 리스트 만들기

# 이메일 -> (사용자 식별자) @ (도메인 주소)
# 이때 "@"로 split하면, 사용자 식별자만 추출 가능하다!

sentence = "사과,바나나,포도"
fruits = sentence.split(',')
print(fruits)

# 원리
# split() : for 문을 이용해서 (구분자) 기준으로 잘라서, 각 문자를 빈 리스트에 append()한다!

for i in fruits:
    print(i)

print()

for i in fruits:
    print(i, end ="")




# 응용 2. .replace() — 특정 글자 바꾸기

# 함수(구분자, 구분자)
# 구분자 = 인자 = 매개변수 = 파라미터

review = "이 서비스는 별로예요"
fixed = review.replace("별로","최고")
print(fixed)



# 실무 1. f-string (포맷팅) — 변수를 문자열 안에 끼워넣기

# 일종의 템플릿

user_name = "클라라"
question = "파이썬 딕셔너리 사용법"
# 실무 예시: 사용자 입력값을 넣어 AI에게 보낼 프롬프트를 자동 생성
prompt = f"{user_name}님이 '{question}'에 대해 질문했습니다. 초보자 눈높이로 답변해주세요."
print(prompt)
# 출력: 클라라님이 '파이썬 딕셔너리 사용법'에 대해 질문했습니다. 초보자 눈높이로 답변해주세요.




# 기초 3. sorted() / .sort() — 순서대로 정렬하기

numbers = [5, 2, 8, 1]
# sorted()
# 터미널 함수 like "len()"
# 파괴적 방식 : 원본이 바뀜

numbers1 = sorted(numbers)
print(numbers1)

# .sort()
# 얘는 어떤 조건일 때만 정렬하도록 지정할 수 있음
# 비파괴적 방식 : 원본은 그대로

numbers.sort()
print(numbers)
print(list(reversed(numbers)))



# 응용 1. 슬라이싱 [시작:끝] — 일부분만 잘라 꺼내기
# 문법: 리스트[시작인덱스:끝인덱스] (끝 인덱스는 포함 안 됨)


# 키오스크의 원리 : 메뉴를 선택 -> 그 인덱스에 해당하는 값을 -> 장바구니에 추가 append()

menu = ["김밥", "라면", "떡볶이", "순대"]
print(menu[0:2])
print(menu[-1])




# 응용 2. .index() / in — 원하는 값 찾기
skills = ["Git", "Python", "OpenAI API"]


# "Python"이 skills에 있어?
print("Python" in skills)   # 결과 = True

# "Python"은 몇번째 칸에 있어?
print(skills.index("Python"))   # 결과 = 1 
# 다만, 고객에게는 +1 을 해서, 2번째라고 설명




# 실무 1. 리스트 컴프리헨션(List Comprehension) — 반복문을 한 줄로

# 실무에서 쓰는 방식이다!

ai_responses = ["네", "안녕하세요! 무엇을 도와드릴까요?", "좋아요", "파이썬 학습을 시작해볼까요?"]

long_responses = [text for text in ai_responses if len(text) >= 10]

print(long_responses)




# 3️⃣ 딕셔너리(Dictionary) 필수 함수 6가지
# 딕셔너리 = 서랍, 진열장

# 기초 1. .get() — 열쇠(key)로 서랍(value) 열기


# 없을 경우 -> None 처리
# therefore, 에러 발생하지 않는다!

student = {"name": "클라라", "course": "AI서비스개발"}
print(student["name"])

# None
print(student.get("age"))

# 출력: 20 (없을 때 기본값 지정 가능)
print(student.get("age", 20))





# 기초 2. .keys() — 모든 이름표(key) 확인하기

student = {"name": "클라라", "course": "AI서비스개발"}
print(student.keys())

# 출력: dict_keys(['name', 'course'])





# 기초 3. .values() — 모든 내용물(value) 확인하기
print(student.values())




# 응용 1. .items() — 이름표와 내용물을 짝지어 순회하기
profile = {"이름": "클라라", "관심분야": "AI 서비스 기획"}

for key, value in profile.items():
    print(f"{key}:{value}")   




# 응용 2. .update() — 내용물 추가/수정하기
user = {"name": "클라라", "level": "초급"}

user.update({"name": "오사카"})
print(user)

user.update({"course": "일본어", "grade": "A"})
print(user)




#  실무 1. 중첩 딕셔너리(Nested Dictionary) 다루기 — 서랍 속의 또 다른 서랍장

# 실무에서는 OpenAI/Gemini 같은 AI API가 돌려주는 JSON 응답이 대부분 이런 중첩 구조
# 카테고리 형태

api_response = {    "id": "chatcmpl-123",   
                    "choices": [ { "message": { "role": "assistant",
                    "content": "안녕하세요! 무엇을 도와드릴까요?"  } 
                     }  
                      ]
                } 


answer = api_response["choices"][0]["message"]["content"]
print(answer)





