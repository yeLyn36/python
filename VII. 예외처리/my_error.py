
class OddError(Exception):
   def __init__(self, message="홀수불가능"):
       self.message = message

   def __str__(self):
       return self.message

n = 11
try:
    if n % 2 != 0:
        raise OddError
    else :
        print("짝수")
except OddError as e:
    print(e)

