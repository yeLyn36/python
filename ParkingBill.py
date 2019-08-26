time = int(input("몇 분 동안 주차하셨습니까? "))
bill = 2000

if time <= 30 :
  print(bill, "원입니다.")
elif time<= 24*60 :
  if (time-3)%10 > 0 : 
    over  = (time-30)//10 + 1
  bill += over*1000
  if bill <= 25000 :
    print(bill, "원입니다.")