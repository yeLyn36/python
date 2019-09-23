f = open('file.txt', "w")

try:
    f.write("hello python\n")
    f.write("100")
except TypeError:
    print("타입 예외 발생 (100은 쓸 수 없음)")
finally:
    print("예외 여부와 상관없이 쓸 수 있음")
    f.close