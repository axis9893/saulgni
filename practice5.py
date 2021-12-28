
# 문자열 입력방법 1
print("나는 %d 살입니다" % 20) # 정수형 입력
print("나는 %s을 좋아해요" %"python") #문자열
print("나는 %s색과 %s색을 좋아해요" % ("파란", " 오렌지"))

#방법 2 

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format ("파란", " 오렌지"))
print("나는 {0}색과 {1}색을 좋아해요" .format ("파란", " 오렌지")) #숫자를 기입하여 순서를 지정 할 수도 있다
print("나는 {1}색과 {0}색을 좋아해요" .format ("파란", " 오렌지")) #숫자를 기입하여 순서를 지정 할 수도 있다


#방법3

print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color = "오렌지")) # 변수를 직접 지정해서 사용할 수 도있다
print("나는 {age}살이며, {color}색을 좋아해요" .format(color = "오렌지", age = 20))

#방법4 python ver 3.6 이상 ~

age = 20
color = "오렌지"
print(f"나는 {age}살이며, {color}색을 좋아해요")