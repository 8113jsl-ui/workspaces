radius = int(input())
height = int(input())
volume = 3.14 * radius**2 * height
print(volume)


number = int(input("숫자를 입력하세요: "))

if number % 2 == 0:
    print(str(number) + "은(는) 짝수입니다.")
else:
    print(str(number) + "은(는) 홀수입니다.")


seconds = int(input("초를 입력하세요: "))
print('현재 시각은 {}:{} 입니다.'.format((seconds//60), (seconds%60)))
print('즉, 현재 시각은 {}분 {}초 입니다.'.format((seconds//60), (seconds%60)))



name = "이재서"
age = 27
height = 168.0
print("이름: " + name + ", " + "나이: " + str(age) + "살, " + "키: " + str(height) + "cm")



price = int(input("상품 가격을 입력하세요: "))
quantity = int(input("수량을 입력하세요: "))
total = price * quantity
print("총 금액: " + str(total))