num = input("숫자를 입력해주세요 : ")
sum = 0

for i in range(len(num)):
  sum += int(num[i])
print(sum)