num_list = [5, 1, 4, 3, 2, 6]
num_list.sort() # 순서 정리
print(num_list)

num_list.reverse() # 순서 뒤집기
print(num_list)

num_list.clear() # 인자 삭제
print(num_list)

num_list = [5, 1, 4, 3, 2, 6]
mix_list = ["유재석", 1, "A"]

#리스트 확장
num_list.sort()
num_list.extend(mix_list)
print(num_list)


