# 리스트[] 
# 순서를 가진 변수

# subway = [10,20,30]
# print(subway)

subway = ["유재석", "박명수", "하하"]
print(subway)

subway.append("정형돈") # 인자를 추가함
print(subway)

subway.insert(1, "정준하") # 인자를 원하는 사이에 넣을 수 있다
print(subway)

print(subway[2])
print(subway[2:])

print(subway.index("박명수"))

print(subway.pop()) # 인덱스를 뒤에서부터 인자를 빼냄
print(subway)

subway.append("유재석")
print(subway)

print(subway.count("유재석"))