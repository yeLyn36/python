#야구 게임
# 세자리 중복 없는 임의의 수 ㅁ나들지
# 무한 반복
# 사용자 입력 받기
# Strike, Ball vkswjd
# 사용자 입력, strike, ball 출력
# 임의의 수, 사용자 입력이 같으면 HIT, break if
import random

#answer = str(random.randrange(100, 999+1))
#random.shuffle(list(range(1, 9+1)))
#answer = ""
#for i in l[:3] :
#  answer += str(i)
#''.join(str(i) for i in l[:3]) -> 위 3개의 문장과 같은 의미

l = random.sample(range(1, 9+1), 3)
answer = ''.join(str(i) for i in l[:3])
#print(answer)

while True :
  player = input("숫자 3자리를 입력하세요 : ")
  strike = 0
  ball = 0
  #스트라이크, 볼 판정
  for i in range (len(answer)) :
    for j in range (len(player)) : 
      if answer[i] == player[j] : 
        if i == j :
          strike += 1
        else :
          ball += 1

  print("{}\tStrike : {}\tBall : {}".format(player, strike, ball))
  if answer == player : 
    print("HIT")
    break
