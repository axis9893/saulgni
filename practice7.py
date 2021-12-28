url = "http://naver.com" #변수 지정

print(url)

my_str = url.replace("http://", "") # 새로운 변수 지정후 http:// 변환하여 공백으로 만든
print(my_str)

my_str = my_str[:my_str.index(".")] # .com 을 인덱스 명령어로 안나오게한 새로운 변수생성
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"  # 
print("{0}의 비밀번호는 {1}입니다." .format(url, password))