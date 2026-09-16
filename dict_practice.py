# [실습 과제]

# 문제 1. dict_a의 결과가 나오도록 빈칸을 채워보세요.

## (1)
dict_a["name"] = "구름"
## (2)
del dict_a["name"]

df


# 문제 2. 딕셔너리와 리스트를 조합해 정보를 출력하기
# 딕셔너리의 리스트를 선언합니다.
pets = [    {"name": "구름", "age": 5},    {"name": "초코", "age": 3},    {"name": "아지", "age": 1},    {"name": "호랑이", "age": 1}]
print("# 우리 동네 애완 동물들")

#TODO: 여기에 반복문을 작성하세요.
for pet in pets:
        print(pet["name"], str(pet["age"]) + "살")




# 문제 3. numbers 내부에 들어있는 숫자가 몇 번 등장하는지 세기

# (방법 1) count()



# 숫자는 무작위로 입력해도 상관 없습니다.
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

# 1. counter의 키 = numbers 리스트의 원소
# 2. counter의 값 = numbers 각 원소의 개수

#TODO: 여기에 코드를 작성하세요.
# 최종 출력
for i in numbers:
    numbers.count(i)
    counter[i] = numbers.count(i)
#    count = 0
#    count += i
#    counter[i] = count

print(counter)



# 문제 3. numbers 내부에 들어있는 숫자가 몇 번 등장하는지 세기

# (방법 2) +=
# dsad
# 숫자는 무작위로 입력해도 상관 없습니다.
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
#TODO: 여기에 코드를 작성하세요.
# 최종 출력
     if number not in counter:
          counter[number] = 1                    # counter에 없던 숫자는 1을 할당하세요! -> 1로 시작하세요!
     else:
          counter[number] += 1                   # counter에 이미 있는 숫자 -> 나올 때마다 1씩 더하세요!
     counter[number] = counter[number]
     
print(counter)




# 문제 4. 자료형을 구분해서 출력하기 (type() 활용)
# 딕셔너리를 선언합니다.
character = {    "name": "기사",    "level": 12,    "items": {        "sword": "불꽃의 검",        "armor": "풀플레이트"    },    "skill": ["베기", "세계 베기", "아주 세게 베기"]}

# for 반복문을 사용합니다.
for key in character:
    #TODO: 여기에 코드를 작성하세요.    
    # (character[key]가 dict이면 그 내부를 한 번 더 반복,    
    #  list이면 그 내부를 한 번 더 반복, 그 외에는 바로 출력)
    if type(character[key]) == dict:
         for keys in character[key]:
              print(keys,":",character[key][keys])
    elif type(character[key]) == list:
         for j in character[key]:
              print(key,":",character[key][character[key].index(j)])
    else:
         print(key,":",character[key])
