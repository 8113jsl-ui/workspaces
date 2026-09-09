# remove()
list_c = [1, 2, 1, 2]
list_c.remove(2)
print(list_c)


# clear()
list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
print(list_d)


# sort() : 오름차순(asd) / 내림차순(des)
list_e = [52, 273, 103, 32, 275, 1, 7]
list_e.sort()               
# 오름차순 정렬        # 기본적으로 sort() 오름차순
print(list_e)


list_e.sort(reverse=True)   
# 내림차순 정렬 (키워드 매개변수 활용)      # reverse = True : 내림차순
print(list_e)



# in / not in
list_a = [273, 32, 103, 57, 52]
print(273 in list_a)
print(99 in list_a)
print(100 in list_a)
print(52 in list_a)


list_a = [273, 32, 103, 57, 52]
print(273 not in list_a)
print(99 not in list_a)
print(100 not in list_a)
print(52 not in list_a)
print(not 273 in list_a)