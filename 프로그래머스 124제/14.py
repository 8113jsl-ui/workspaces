# 배열에서 문자열 대소문자 변환하기

def solution(strArr):
    answer = []
    while True:
        for i in range(len(strArr)):
            if i%2 != 0:
                strArr[i] = strArr[i].upper()
                answer.append(strArr[i])
            elif i%2 == 0:
                strArr[i] = strArr[i].lower()
                answer.append(strArr[i])  
        break
                
    return answer