# 문자열 · 리스트 · 딕셔너리 핵심 함수 테스트
# 🟢 기초  — 함수 하나씩 정확히 익히기


# 문제 1. 문자열 대문자/소문자로 바꾸기
word = "Learn Python"
# word를 모두 대문자로 바꾼 결과와, 모두 소문자로 바꾼 결과를 각각 출력하세요.

upper = word.upper()
print(upper)

lower = word.lower()
print(lower)



# 문제 2. 문자열 앞뒤 공백 제거하기
text = "   Python Programming   "

# text의 앞뒤 공백을 제거한 결과를 출력하고, 공백을 제거한 문자열의 길이(글자 수)도 함께 출력하세요.
trimmed = text.strip()
print(trimmed)
print(len(trimmed))




# 문제 3. 리스트에 값 추가하고 정렬하기
numbers = [5, 3, 8, 1]

# numbers에 10을 추가한 뒤, 오름차순으로 정렬해서 출력하세요.
numbers_a = numbers.append(10)
print(sorted(numbers))




# 문제 4. 리스트에서 특정 값의 위치와 개수 찾기 - count() 함수
fruits = ["apple", "banana", "apple", "cherry", "apple"]

# "apple"이 리스트에서 처음 등장하는 인덱스(위치)와, 총 몇 번 등장하는지(개수)를 각각 출력하세요.

print(fruits.index("apple"))

apple = fruits.count("apple")
banana = fruits.count("banana")
cherry = fruits.count("cherry")

print("apple:", str(apple))
print("banana:", str(banana))
print("cherry:", str(cherry))



# 문제 4. 리스트에서 특정 값의 위치와 개수 찾기
fruits = ["apple", "banana", "apple", "cherry", "apple"]
apple_idx = fruits.index("apple")
apple_count = fruits.count("apple")
print(apple_idx)
print(apple_count)

#컴프리헨션 리팩토링 
apple_idx = next(i for i, v in enumerate(fruits) if v == "apple")
apple_count = sum(1 for v in fruits if v == "apple")        # v가 "apple"일 때 1씩 누적해줘!
print(fruits[apple_idx], ":", apple_count)




# 문제 5. 딕셔너리에서 값 꺼내고 키 목록 확인하기
info = {"name": "김민수", "age": 25, "job": "학생"}

# "age" 키에 해당하는 값을 get()으로 꺼내 출력하고, info가 가진 모든 키의 목록을 출력하세요.

print(info.get("age"))
print(info.keys())



# 강사님 방식
keyset = info.keys()
for key in keyset:
    print(key)

print(keyset)

print(list(info.keys()))





# 🟡 응용  — 여러 함수를 조합해서 활용하기

# 문제 6. 문자열 나누고 다시 합치기
sentence = "사과,바나나,포도,딸기"

# 쉼표(,)를 기준으로 sentence를 나눠 리스트로 만든 뒤, 그 리스트를 " - "(공백-하이픈-공백)로 다시 이어 붙여 하나의 문자열로 출력하세요.
# 예상 출력 형태: 사과 - 바나나 - 포도 - 딸기

list = sentence.split(',')


# '문자'.join() : 문자 로 합쳐줘!

result = " - ".join(list)
print(result)





# 문제 7. 점수 기준으로 내림차순 정렬하기
scores = [("철수", 85), ("영희", 92), ("민수", 78)]

# ( , ) : 튜플
# 그런데 이 경우, 튜플을 해체해서, 딕셔너리 key : value 형태로 변환하는 게 더 유용하다
# 특히 json 파일을 만들기 위해서는 딕셔너리가 좋다.

# scores를 점수(튜플의 두 번째 값)가 높은 순서대로 정렬해서 출력하세요.

a = ("철수", 85)
print(a[0])

scores_a = []

for i in scores:
    if i[1] >= 90:
        scores_a.append(i[1])
    elif i[1] >= 80:
        scores_a.append(i[1])
    elif i[1] >= 70:
        scores_a.append(i[1])
    print(scores_a.sort())



print(sorted(scores_a, reverse=True))


# 딕셔너리로 출력하기
dict = {}

for j in scores:
    dict[j[0]] = j[1]

print(dict)


# 딕셔너리 출력하기 - 클래스
# 1단계 : 딕셔너리로 재구성 dict() 생성자 활용
scores = [("철수", 85), ("영희", 92), ("민수", 78)]

scores_dict = dict(scores)
print(scores_dict)


# items() 활용하여 점수값 기준으로 내림차순 정렬

def get_score(item):        # def : 함수 정의  /  get_score : 함수 이름  /  item : 매개변수(파라미터)
    return item[1]


scores_dict = dict(scores_dict.item(), key = get_score, reverse = True)
print(scores_dict)







# 문제 8. 두 딕셔너리 병합하기
menu1 = {"커피": 4000, "라떼": 4500}
menu2 = {"라떼": 5000, "쿠키": 3000}

# menu1을 기준으로 menu2의 내용을 합쳐(겹치는 키 "라떼"는 menu2의 값으로 덮어써서) 하나의 딕셔너리로 만들고, 그 결과를 items()로 반복하며 "메뉴명: 가격" 형태로 한 줄씩 출력하세요.



# update()
new_menu = {}
new_menu.update({"커피": menu1["커피"], "라떼": menu2["라떼"], "쿠키": menu2["쿠키"]})

for key, value in new_menu.items():
    print(f'{key}: {value}')



# 값을 바꾸되,
# 기존에 있는 데이터를 백업해놓고 싶다
# copy()
menu1 = {"커피": 4000, "라떼": 4500}
menu2 = {"라떼": 5000, "쿠키": 3000}

merged = menu1.copy()
merged.update(menu2)

for name, price in merged.item():
    print(f'새롭게 리뉴얼된 메뉴 {name} : {price}')

print(menu1)
print()
print(menu2)

# 컴프리헨션 방식
merged2 = {k:v for d in (menu1,menu2) for k,v in d.items()}
print(merged2)





# 문제 9. 문장에서 단어 개수와 가장 긴 단어 찾기
sentence = "Python is a powerful and easy programming language"

# 이 문장이 총 몇 개의 단어로 이루어져 있는지와, 그중 가장 긴 단어가 무엇인지 각각 출력하세요.

# 1단계 : split() 함수로 잘라내기
# 2단계 : split()의 결과 -> 리스트 []
# 3단계 : 


list = sentence.split(" ")
count = 0

for i in list:
    if len(i) >= 1:
        count += 1
    else:
        count += 0

print("총 단어 수: ")
print(count)

print(list)

max = list[0]

for word in list:
    if len(max) <= len(word):
        max = word
    else:
        max = max

print(max)


# 강사님 풀이 
# 1. split()

# longword = word[0]
# for v in words:
#     if len(v) > len(longword):
#         longword = v
#     else:
#         longword = longword

# 2. max() 함수
sentence = "Python is a powerful and easy programming language"
words = sentence.split()    # 리스트
print(max(words))



lengths = [len[w] for w in words]

longest = words[lengths.index(max(lengths))]       # 앞의 lengths -> 클래스
# class : 데이터 + 처리
print(len(words), longest)









# 문제 10. 단어별 등장 횟수 세기 (빈도수 계산)
text = "apple banana apple cherry banana apple"

# text를 단어 단위로 나눈 뒤, 각 단어가 몇 번씩 등장하는지 딕셔너리 형태로 만들어 출력하세요.
# 예상 출력 형태: {'apple': 3, 'banana': 2, 'cherry': 1}

list = text.split(" ")

print(list)


apple = list.count("apple")
banana = list.count("banana")
cherry = list.count("cherry")



dict = {}
dict["apple"] = apple
dict["banana"] = banana
dict["cherry"] = cherry


print(dict)



# 새 풀이

# 1. count = 딕셔너리 생성
text = "apple banana apple cherry banana apple"
count = {}
number = 0

# 2. 문자열을 공백 기준으로 split()로 잘라야겠다!
text = "apple banana apple cherry banana apple"
# split()의 결과 = 리스트 형식이다!
list = text.split()

number = 0
# 3. 자른 단어의 개수가 각각 몇 개인지를 세야 한다.




# 아이디어 1. count() 함수

# 아이디어 2. for 문으로, text.split()에서 단어가 등장할 때마다 +1을 한다
# for i in list:
#     for j in range(len(list)):
#         if list[j] == i:
#             number += 1

# print(number)




text = "apple banana apple cherry banana apple"
#1 count = 딕셔너리 생성 
count = {}
#2 문자열 공백을 기준으로 split() => 리스트로 생성 
words = text.split()    #단어 단위로 나눠서 리스트 생성

#3 분리된 단어별 횟수를 센다
for w in words:    #단어를 하나씩 순서대로 확인 
    if w in count:
        count[w] = count[w]+1
    else:
        count[w] = 1

 

#4 count 딕셔너리 출력
print(count)




