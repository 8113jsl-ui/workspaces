tuple_test = 10, 20, 30, 40
print("괄호가 없는 튜플의 값과 자료형 출력")

print("tuple_test:", tuple_test)
print("tuple_test Type:", type(tuple_test))

# 파이썬에서 모든 Type -> 클래스(Class)로 저장
# 클래스 = 데이터 + 행위
# 클래스는 무한히 복제(Cloning)할 수 있다. 


# 괄호가 없는 튜플  tuple_test01에 자신의 이름과 친구 2명의 이름을 할당, 출력
tuple_test01 = "이재서", "초아", "이현종", "박영준"
print("tuple_test01:", tuple_test01)


# 본인 이름과 친구들 이름을 순서대로 출력
# for 활용
for i in range(len(tuple_test01)):
    print(tuple_test01[i])
# -> 더 느리긴 하지만
# -> 데이터 변경사항을 인덱스 위치까지 확인하면서 비교할 수 있다


for name in tuple_test01:
    print(f"이름 : {name}")
# -> 데이터가 많아질 때, 더 유리
# -> 속도가 더 빠르다
# -> 내부 반복자를 이용해서 추출기(iterator)가 바로 데이터를 처리해서 뽑아낸다
# -> 코테에서 더 유리!!!!!

# iterator
# enumerator


