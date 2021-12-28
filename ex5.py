# quiz
from random import *
user_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
user = range(1, 21) # 1~ 20 숫자 생성

print("user_list",type(user_list))

shuffle(user_list)
print(user_list, type(user_list))

print(type(user)) # type range로 되어있음.

user = list(user) # type을 list로 변환
print(type(user))
print(user)

shuffle(user)
print(user)

winners = sample(user, 4)

print (" === 당첨자 발표 ===")
print("치킨 당첨자",winners[0])
print("커피 당첨자", winners[1:])
print("===축하합니다===")