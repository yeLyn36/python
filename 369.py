number = []

for i in range(99) : 
  number.append(i+1)

for i in range(99) : 
  if number[i] < 10 : #1의 자리 수
    if number[i] % 3 == 0 : #3의 배수일 경우
       print('짝')
    else :
      print(number[i])
  else :
    if (number[i]//10) %3 == 0 and (number[i]%10) %3 == 0 and number[i]%10 != 0: 
      print('짝짝') #10의 자리이면서 10의 자리가 3의 배수이고 1의 자리가 3의 배수인 경우 / 33,, 36, 39, 63, 66, 69, 93, 96, 99
    elif (number[i]%10) %3 == 0 or (number[i]//10) %3 == 0 and number[i]//10 != 0 : 
      print('짝') # 1자리 숫자가 3의 배수이거나 10자리 숫자가 3의 배수인 수 / 13, 16, 19, 23, 26, 29, 30, 31 .. 38, 43, ..., 98
    else :
      print(number[i])