import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("이름 : " + self.name + "\n나이 : " + str(self.age))

f = open("person_data.bin", "wb")

p = Person("원예린", 18)

pickle.dump(p, f)   #p객체를 f파일로 저장
f.close()

#Load

f = open("person_data.bin", "rb")

person1 = pickle.load(f)
print(person1)

f.close()

#save object list
#p240

p1 = Person("윤정한", 24)
p2 = Person("우도환", 27)
p3 = Person("민윤기", 26)
people = [p1, p2, p3]
f = open("people_data.bin", "wb")
pickle.dump(people, f)
f.close()

#Load

f = open("people_data.bin", "rb")
peo = pickle.load(f)
f.close()

sum = 0
for p in peo:
    print(p)
    sum += p.age
print(sum)

# f = open("savefile.per", "r", encoding="utf8")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     a = line.split("\t")
#     print(a[])