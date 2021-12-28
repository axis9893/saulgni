
#사전, 딕셔너리

cabinet = {3: "이순신", 100:"안중근"} #원하는 번호에 인자를 저장한 경우

# 값을 출력하는 방법
print(cabinet[3]) 
print(cabinet.get(3))

# 없는 값을 출력할때 방법

# print(cabinet[5]) #없는 번호를 출력할 경우 에러가 나면서 더이상 진행이 안되고 멈춤
print(cabinet.get(5)) # 없는 번호이지만 none을 출력하고 프로그램은 진행됨

print(cabinet.get(5, "사용가능")) #없는 번호이지만 원하는 문자를 출력할 경우 '사용가능'을 출력함

print(3 in cabinet)  # True 값을 출력
print(5 in cabinet)  # False 값을 출력

#cabinet = {"A-1" : "이순신", "B-1" : 100 "안중근"} #원하는 번호에 인자를 저장한 경우