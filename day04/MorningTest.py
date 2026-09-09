# [기초]

# 1. 리스트 합계 구하기
numbers = [12, 25, 7, 33, 18]
total = 0

for i in numbers:
    total += i

print(total)


# 강사님 풀이
numbers = [12, 25, 7, 33, 18]
total = 0

# total = 0 + numbers[0]
# print(total)

# total = total + numbers[1]      # 코드는 위 -> 아래 순서로 실행된다. 따라서 total에 새로운 값을 덮어쓸 수 있다.
# total = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
# 그러나, 위 방법은 리스트가 백 개, 만 개가 되면 쓸 수 없다.

print()         # 한 줄 띄우기

저금통 = 0
for number in numbers:
    저금통 = 저금통 + number

print(저금통)

    

# 2. 리스트 평균 구하기
numbers = [12, 25, 7, 33, 18]
total = 0

for i in numbers:
    total += i

avrg = 0
for j in numbers:
    avrg = total/len(numbers)

print(avrg)




# 3. range()로 구구단 3단 출력하기
for i in range(1,10):
    print(f"3 * {i} = {3*i}")



# 4. 리스트에서 최댓값 찾기 (내장함수 없이- 사용자가 입력한 랜덤값 10개)

# 랜덤한 10개의 값을 입력받기 -> input() 10번

list = []

for i in range(11):
    int(input()) = list[i] 
    list = list.append(list[i])


# 재경님 방식
list_a = [1,2,3,4,5,66,7,8,5,42]

max = list_a[0]     # 리스트 첫번째 값 -> 비교 시작점으로 만들었음
for number in list_a:
    if max >= number:
        max = max
    else:
        max = number

print(max)


# 5. 딕셔너리 순회하며 출력하기
# 아래 딕셔너리를 "키: 값" 형태로 한 줄씩 출력해보세요.
character = {"name": "기사", "hp": 200, "mp": 30, "level": 5}

for key in character:
    print(key,":",character[key])


# 강사님 방식
character = {"name": "기사", "hp": 200, "mp": 30, "level": 5}
char_name = character["name"]
char_hp = character["hp"]
char_mp = character["mp"]
char_level = character["level"]

# for : 자동 패치(fetch)기
# movie라는 딕셔너리를 생성하고, 위에서 각각 담아 놓은 5개의 데이터를 movie에 저장하세요.
movie = {}

movie["name"] = char_name
movie["hp"] = char_hp
movie["mp"] = char_mp
movie["level"] = char_level

print(movie)
print('{}'.format("name"+" : "+movie["name"]))


# 딕셔너리.items() : 키와 값을 한꺼번에 가져올 수 있다
for key, value in movie.items():       # key : movie 딕셔너리의 키를 전부 가져오겠다
    print("{} : {}".format(key,value))



# 6. while로 1부터 5까지 출력하기
number = 0 # 시작점

while number <= 4:
    number += 1
    print(number)


# 6. break 사용
number = 0 # 시작점

while number <= 4:
    number += 1
    print(number)
    if number == 6:
        break


# 6. 무한루프 형식 : "실무에서 쓰는 방식"
number = 1

while True:
    if number > 5:
        break
    print(number)
    number += 1
    


# 7. 리스트에서 짝수 개수 세기
numbers = [3, 8, 15, 22, 7, 40, 11]
# 1. 리스트를 접근해서 값을 가져와서 짝수 검증한다
n1 = numbers[0]
result = n1%2
print(result)

if result == 1:
    print("홀수")
else:
    print("짝수")

# 2. 1과 같은 메커니즘으로 아래의 코드의 흐름을 짜면 된다

# 시작점을 만든다
count = 0 

# numbers 리스트의 모든 요소에 대해, 짝수/홀수 검증한다
for i in numbers:
    if i%2 == 0:
        count += 1
    else:
        count += 0

print("짝수의 개수: ", count, "개", sep = "")




# 7-1. Sum() 함수
numbers = [3, 8, 15, 22, 7, 40, 11]
count = sum(1 for number in numbers if number %2 == 0)
      # sum(1 ~) : 1은 치사값 

print(count)




# 8. 문자열 거꾸로 출력하기

# 강사님 설명
word = "Python"
for ch in reversed(word):
    print(ch, end ="")

# 내 코드
word = "Python"

word_reversed = list(reversed(word))
for i in word_reversed:
    print(i, end = "")


# 실무 코드! : ''.join(reversed())
result = ''.join(reversed(word))
print(result)

result = ''.join(word)
print(result)




# 9. 리스트에서 특정 값의 인덱스 찾기 (break 활용)

# 57이라는 값이 몇 번째 인덱스에 있는지 break를 사용해 찾아보세요
# 원하는 값이 나오면 더 이상 반복문 돌리지 않기! (원하는 값 나오면 -> 멈춤)
# 선형 탐색 (Linear Search)


# 내 풀이
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    if array[i] == "57":
        break

print(f'57은 {i-1}번째 인덱스에 있습니다.')

print(range(len(array)))


# Method 1: Range()
array = [273, 32, 103, 57, 52]
#method-1 : range()
t_number = 57
idx = -1
for i in  range(len(array)):
    if array[i] == t_number:
        idx = i
        break
print(idx)
        


# Method 2: enumerate()   ------ 리스트의 인덱스 & 값 둘다 가져오는 함수
for i, v in enumerate(array):
    if v == t_number:
        print(i)
        break
    else:
        print(-1)       # -1 : 더 이상 찾을 수 없다
        



# 10. 1부터 100까지의 합 구하기 (while)
total = 0
list = list(range(1,101))

while True:
    for i in list:
        total += i
    if i in list:
        print(total)
    break



# 가우스 덧셈공식 = n*(n+1)/2
number = 100
total= = number*(number+1)/2
print(total)

# 재경님
i=1
result=0
while i<=100:
    result=result+i
    i+=1
print(result)


# 혜윤님
i = 0
s = 0
while i <= 100 :
    s += i
    i += 1
print(s)








# [중급]
# 11. 구구단 2~9단 전체 출력하기 (중첩 for)

numbers = [2,3,4,5,6,7,8,9]
multiply = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    for j in multiply:
        print(f'{i} * {j} = {i*j}')

# 2*1=2 / 2*2=4 / ~~~

for dan in range(2,10):
    print("===={dan}====")
    for i in range(1,10):
        print(f'{dan} * {i} = {dan*i}')
    print()


# while 문을 이용하기
dan = 2

while dan <= 9:
    i = 1
    while i <= 9:
        print('{} * {} = {}'.format(dan, i, dan*i))
        i += 1
    dan += 1




# 12. FizzBuzz 문제
# 조건의 순서가 중요!!!!
# 1부터 30까지 숫자를 출력하되, 3의 배수면 "Fizz", 5의 배수면 "Buzz", 둘 다의 배수면 "FizzBuzz"를 출력해보세요.

for i in range(1,31):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else: 
        print(i)


# 조건 순서가 다른 경우 : FizzBuzz로 가기도 전에, Fizz에서 걸러진다
# 따라서 의도한 대로 코드가 실행되도록, 조건의 순서 배치해야 한다.
for i in range(1,31):
    if i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    elif i%15 == 0:
        print("FizzBuzz")
    else: print(i)




# 13. 짝수만 필터링해서 새 리스트 만들기

# 유형 : 필터링 문제 => 조건에 맞는 요소만 골라내는 작업
numbers = [3, 8, 15, 22, 7, 40, 11, 6]
even = []

for i in numbers:
    if i%2 == 0:
        even.append(i)

print(even)


# 리스트 컴프리헨션 방식 (list comprehension) 
even_list1 = [n for n in numbers if n%2==0]
print(even_list1)




# 14. 두 리스트로 딕셔너리 만들기 (range 활용)
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

# 같은 길이의 리스트
# 같은 인덱스의 요소들끼리 Pairing하면 된다
# 인덱스 번호를 공유해서 쓴다!

new_dict = {}

for i in range(4):  # range(len(key_list))
    new_dict[key_list[i]] = value_list[i]
    # key_list[인덱스]       value_list[인덱스]

print(new_dict)

print()
print()

# zip() 함수
new_dict1 = dict(zip(key_list, value_list))  # dict() : 생성자 (딕셔너리 원형)
print(new_dict1)




# 15. 리스트 중복 제거하기 (반복문)
numbers = [1, 3, 2, 3, 5, 1, 4, 2]

# 설계
# 리스트를 1열씩 좌 -> 우로 진행하며, 새로운 값을 채택한다
# 만약, 이미 나온 값이라면 채택하지 않는다.

for number in numbers:
    if count(number) <= 1:
        numbers = numbers.append(number)
    else:

print(numbers)


# 설계 2
# numbers 리스트에서 중복되는 값을 뺀다 - remove()
# 빼는 값은 2번 이상 등장하는 값 중 1개만 남긴다.




# 16. 별 삼각형 만들기 (오름차순)

# *
# **
# ***
# ****
# *****




# 17. 별 삼각형 만들기 (내림차순, 역삼각형)




# 18. 리스트 최댓값/최솟값 동시에 찾기




# 19. 딕셔너리에서 조건을 만족하는 키만 추출하기




# 20. while + break: 누적합이 목표값을 넘는 순간 찾기



# 22. 소수(prime number) 판별하기



# 23. 문자열 내 특정 문자 개수 세기




# 24. 버블 정렬로 리스트 오름차순 정렬하기
# 25. continue로 3의 배수를 제외한 합 구하기
# 26. 딕셔너리 리스트에서 최고 점수 학생 찾기
# 27. range 3개 매개변수로 짝수의 합 구하기
# 28. 리스트에서 두 번째로 큰 값 찾기
# 29. while로 팩토리얼 계산하기
# 30. 학생 성적 데이터에서 과목별 평균 구하기
