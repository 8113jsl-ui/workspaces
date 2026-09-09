dictionary = {'name': '8D 건조 망고', 
           'type': '당절임', 
           'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'], 
           'origin': '필리핀', 'price': 5000}

dictionary["price"] = 6000

print(dictionary)


# CRUD : 자료구조에서 반드시 갖춰야 할 구조

del dictionary["price"]
print(dictionary)
# print(dictionary["price"])    ----> KeyError



# 딕셔너리를 선언합니다.
dictionary_1 = {}         # {} : 빈 딕셔너리 선언 
# 요소 추가 전에 내용을 출력해 봅니다.
print("요소 추가 이전:", dictionary_1)
# 딕셔너리에 요소를 추가합니다.
dictionary_1["name"] = "새로운 이름"
dictionary_1["head"] = "새로운 정신"
dictionary_1["body"] = "새로운 몸"
# 출력합니다.
print("요소 추가 이후:", dictionary_1)