# 1. 문자열 길이 구하기 (함수)
a = "Life is too hard"
b = len(a)
print(b)



# 2. 인덱싱 : 가리킨다 / 슬라이싱 : 잘라낸다
print(a[5])
print(a[5:6])
print(a[-4])
print(a[-0])             # -0은 존재 x / 0과 동일
print(a[15])
print(a[15:16])



# 3. 슬라이싱
d = "Life is short, you need Python"
e = d[0]+d[1]+d[2]+d[3]
k = d[0:4]
h = d[15:30]

print(e)
print(d[0:4])
print(k)
print(h)


print('\"'+"C"+":\\"+"Download"+"\\"+"\'"+"hello"+"\'"+"."+"py"+'\"')