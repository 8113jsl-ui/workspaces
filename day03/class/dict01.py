{    "키A": 10,      
    # 문자열을 키로 사용하기
     "키B": 20,
     "키C": 30,    
     1: 40,          # 숫자를 키로 사용하기    
     False: 50       # 불(bool)을 키로 사용하기
 }

# 딕셔너리
# 형태 = 키: 값, key: value
# value -> 텍스트, 이미지, 사운드, 영상, 리스트 등이 들어갈 수 있다
# key -> 숫자, 문자열, 불린
# 요즘 세상에 딕셔너리는 더 유용한 구조


dict_a = {  "name": "어벤저스 엔드게임",    "type": "히어로 무비"}

print(dict_a["name"])
print(dict_a["type"])


dict_b = {'director': ['안소니 루소', '조 루소'], 'cast': ['아이언맨', '타노스', '토르', '닥터스트레인지', '헐크']}
print(dict_b['director'])


# 딕셔너리를 선언합니다.
dictionary = {    "name": "7D 건조 망고",    "type": "당절임",    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],    "origin": "필리핀"}
# 출력합니다.
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()
# 값을 변경합니다.
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])


print(dictionary["ingredient"])
print(dictionary["ingredient"][1])