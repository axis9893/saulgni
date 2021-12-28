station = "사당"

print(station + " 행 열차가 들어오고 있습니다")

print( 10 > 3)
print ( 10 < 3)

print ( 1 != 3)
print ( not 3 < 1)

print(abs(-5))
print(pow(4, 2)) #4^2 = 4*4 = 16

print(max(5, 12))
print(min(5, 12))

from random import *

print(random())
print (int(random()))

print(int(random() * 45) +1)

print(randrange(1, 46))

date = randint(4, 28)
print("오프라인 모임 매월 " + str(date) + "입니다")


jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("년도 : " + jumin[0:2])
print("월 : " + jumin[2:4])



