# dice1.py

import random

# def rolling_dice() :
#   n = random.randint(1,6)
#   print("6면 주사위 굴린 결과 =", n)

# def rolling_dice(pip) :
#   n = random.randint(1,pip)
#   print("6면 주사위 굴린 결과 =", n)

def rolling_dice(pip, repeat) :
  for r in range(1, repeat+1) :
    n = random.randint(1, pip)
    print(pip, "면 주사위 굴린 결과", r, ":", n)

rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0)
rolling_dice(20, -3)
print()

# star1.py

def star() :
  print("*****")
  # 아무것도 없으면 pass

star()
star()
star()

# varg.py

# print("♥")
# print("♥", "♪")    
# print("♥", "♪", "♣")
# print("♥", "♪", "♣", "♠")
# print("♥", "♪", "♣", "♠", "★")

# varg2.py
# def p( *arg ) :
#   string=""
#   for a in arg:
#     string += (a + " ")
#   print(string)

# p("♥")
# p("♥", "♪")    
# p("♥", "♪", "♣")
# p("♥", "♪", "♣", "♠")
# p("♥", "♪", "♣", "♠", "★")

# varg3.py
def p(space, space_num, *args) :
  string = args[0]
  for i in range(1, len(args)) :
    string += (space * space_num) + args[i]
  print(string)

p(",", 3, "♥", "♪")
p("☆", 2, "♥", "♪", "♣")
p("_", 3, "♥", "♪", "♣", "♠")
print()

# star2.py
def star2(string, *args) :
  for i in range(len(args)) :
    print(string * args[i])

star2("♬", 3)
star2("♡", 1, 2, 3)
print()


# keyfn.py
def fn (a, b, c, d, e) :
  print(a, b, c, d, e)

fn(1, 2, 3, 4, 5)
fn (10, 20, 30, 40, 50)
fn(5, 6, 7, 8, 9)
fn(a=1, b=2, c=3, d=4, e=5)
fn(e=5, d=4, c=3, b=2, a=1)
fn(1, 2, c=3, e=5, d=4)
# fn(e=5, d=4, 1, 2, 3) 에러
print()


# star3.py
# ***__***
# ***__***
# ***__***

def star3 (mark, repeat, space, space_repeat, line) :
  string = ""
  string += (mark * repeat) + (space * space_repeat) + (mark * repeat)
  for i in range(line) :
    print(string)
  print()

star3("*", 3, "_", 2, 3)

# default_args1.py

def hello(msg = "안녕하세요!") : 
  print(msg)

hello("얼마만이냐!")
hello("보고 싶었어")
hello()
print()

# default_args2.py

def hello2(name="원예린", msg = "안녕"):
  print(name+"님", msg + "!!")

hello2("김수진", "하이")
hello2("너")
hello2()
print()

# default_args4.py

def fn2(a, b=[]) :
  b.append(a)
  print(b)

fn2(3)
fn2(5)
fn2(10)
fn2(2, [1])
print()

# default_args5.py

def gugudan(dan = 2) :
  for i in range(1, 9+1) :
    print(dan, "X", i, "=", dan*i)

gugudan(3)
gugudan(2)
gugudan()
print()

# sum.py

def sum(*numbers) :
  sum_value = 0
  for number in numbers:
    sum_value += number
  return sum_value

result = sum(1, 3)
print("1 + 3 = " + str(result) )
print("1 + 3 + 5 + 7 = " + str(result))
print()

def min (*numbers) :
  min_value = numbers[0]
  for number in numbers :
    if number < min_value :
      min_value = number
  return min_value

print("min(3, 6, -2) =", min(3, 6, -2))

def max (*numbers) :
  max_value = numbers[0]
  for number in numbers :
    if number > max_value :
      max_value = number
  return max_value

print("max(8, 1, -1, 12) =", max(8, 1, -1, 12))

def multi_num(multi, start, end) :
  answer = []
  for i in range(start, end+1) :
    if i % multi == 0 :
      answer.append(i)
  return answer

print("multi_num(17, 1, 200) =", multi_num(17, 1, 200))
print("multi_num(3, 1, 100) =", multi_num(3, 1, 100))

def min_max(*args) : 
  min_value = args[0]
  max_value = args[0]
  for a in args : 
    if min_value > a :
      min_value = a
    if max_value < a :
      max_value = a
  return min_value, max_value

min_num, max_num = min_max(52, -3, 23, 69, -21)
print("최솟값 :", min_num, "최댓값 :", max_num)  