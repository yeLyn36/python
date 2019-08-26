numbers = {1, 4, -2, 0, 6}
print(numbers, "중 가장 큰 수는", max(numbers))
print(numbers, "중 가장 작은 수는", min(numbers))
print(numbers, "의 합계는", sum(numbers))   
print("2의 10제곱은", pow(2,10))

pi = 3.141592
print(pi,"의 소수점 1자리 반올림은", round(pi))
print(pi,"의 소수점 1자리 반올림은", round(pi, 0))
print(pi,"의 소수점 2자리 반올림은", round(pi, 1))
print(pi,"의 소수점 3자리 반올림은", round(pi, 2))
print(pi,"의 소수점 4자리 반올림은", round(pi, 3))

# user_name = input("이름은?")
# user_age = input("나이는?")
# print(user_name+"님! 나이는 "+str(user_age)+"세군요!")
# say = "{}님! 나이는 {}세군요!"
# print(say.format(user_name, user_age))
# say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요!"
# print(say.format(user_name, user_age))
# say = "{name}님! 나이는 {age}세군요! {age}세라니 놀라워요!"
# print(say.format(name=user_name, age=user_age))

pi = "3.14159"
print("문자열 출력: "+pi)
print("실수 변환 출력: ",float(pi))
print(float(pi)+100)
year = "2019"
print("올해 연도 : ", year)
print("100년 뒤에는 ", int(year)+100, "년입니다.")
print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
print("올해는 "+ year+"년입니다.")

list = ['d', 'c', 'a', 'b']
list.reverse()
print("리스트 항목 순서 뒤집기", list)
list.sort()
print("리스트 항복 정렬하기", list)
list.sort(reverse=True)
print("리스트 항복 역정렬하기", list)
for index, value in enumerate(list):
  print("인덱스", index, "위치 값은 ", value)

# str="나는 문자열"
# print(str)
n = 3
print(str(n))
#변수명에 사용하면 안되는 것
#keyword
#내장함수명 (권장 안함)

#사용자 정의 함수
def input(s):
  print(s)

input("현재의 input()함수는 사용자 정의 함수입니다.")
