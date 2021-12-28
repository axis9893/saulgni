 # 집합 (set)
 # 중복 안됨, 순서 없음

my_set = {1,2,3,3,4}
print(my_set)
java = {"유재석", "김태호", "박명수"}
python = set(["유재석", "하하"])

 # 교집합 ( java 와 python  양쪽 모두다 포함되어있는 인자)

print(java & python) 
print(java.intersection(python)) 

# 합집합 (java 와 python 양쪽 모두)
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

python.add("정준하")
print(python)