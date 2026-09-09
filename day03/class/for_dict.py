# 딕셔너리를 선언합니다.
dictionary = {    "name": "7D 건조 망고",    
              "type": "당절임",    
              "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],    
              "origin": "필리핀"}

for key in dictionary:      # key in dictionary 했을 때 -> key는 자동으로 dictionary의 element에 대응된다.
    if key == "ingredient":
        for i in range(4):
            print(key,":",dictionary["ingredient"][i])
    else: 
        print(key,":",dictionary[key])