korea = int(input('국어 성적을 입력하세요 :'))
math = int(input('수학 성적을 입력하세요 :'))
english = int(input('영어 성적을 입력하세요 :'))
print("입력받은 성적\n")
print("-----------------\n")
print("국어성적 : {0} \n수학성적 : {1} \n영어성적 : {2}"
          .format(korea, math, english))
print("-----------------\n")
sum = korea + math + english
average = (korea +math+english)/3
print("총점 : ", sum)  
print("평균 : ", average)