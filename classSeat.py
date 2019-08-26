import random
random.random()

classroom = []
num = 0
answer = 0

lastNum = int(input("끝 번호를 입력해주세요 : "))
for i in range(1, lastNum+1) : 
  classroom.append(i)
# classroom = list(range(1, lastNum+1))

while(True) : 
  delNum = int(input("제외할 번호를 입력해주세요 (없으시다면 0을 입력해주세요.): "))
  if(delNum == 0) : 
    break
  else :
    classroom.remove(delNum)
    num += 1

classNum = [i for i in range(1, lastNum+1-num)]

random.shuffle(classroom)

print("자리\t번호")
for i in range(len(classNum)) :
  print(classNum[i], "\t", classroom[i])