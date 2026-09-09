# 딕셔너리를 선언합니다.
dictionary = {    "name": "7D 건조 망고",    "type": "당절임",    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],    "origin": "필리핀"}

# 1. 사용자에게 key 입력받기
key_search = input("제품 항목을 입력하세요: ")

# 2. 입력받은 key 있는 경우 / 입력받은 key 없는 경우
if key_search in dictionary:    # key가 dictionary에 있다면
    print("존재하는 키입니다!", dictionary[key_search])
else:
    print("존재하지 않는 키입니다!")
    