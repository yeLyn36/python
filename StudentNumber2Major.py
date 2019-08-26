#학번을 입력받아 학과 출력하기

studentNumber = input("학번을 입력해주세요 : ")

grade = studentNumber[0]
classroom = studentNumber[1]

#if grade == "1" or grade == "2":
#  if classroom == "1" or classroom == "2":
#    print("뉴미디어소프트웨어과")
#  elif classroom == "3" or classroom == "4":
#    print("뉴미디어웹솔루션과")
#  elif classroom == "5" or classroom == "6":
#    print("뉴미디어디자인과")
#elif grade == "3" :
#  if classroom == "1" or classroom == "2":
#    print("인터랙티브미디어과")
# elif classroom == "3" or classroom == "4":
#    print("뉴미디어디자인과")
#  elif classroom == "5" or classroom == "6":
#    print("뉴미디어솔루션과")

major = [["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"], ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"], ["인터랙티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]]

grade = int(grade)
classroom = int(classroom)  
print(major[grade-1][(classroom-1)//2])
