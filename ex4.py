# 자료구조의 변경
# 커피숍

menu = {"커피", "우유", "쥬스"}  # type set 대괄호
print(menu, type(menu)) 

menu = list(menu)  # type list 중괄호
print(menu, type(menu))

menu = tuple(menu) #type tuple 소괄호
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))