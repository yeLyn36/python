dan = 2
for i in range(1, 9+1):
  print (dan, " * ", i, " = ", i*dan)

for i in range(2, 9+1):
  for j in range(1, 9+1):
    if j > 7 :
      break
    if j % 2 == 0 :
      continue
    print (i, " X ", j, " = ", i*j)
  print("--------------------------------------")