f = open("file.txt", 'r', encoding="utf-8")

text0= f.readline()
print(text0)
text1= f.readline()
print(text1)

f.close()