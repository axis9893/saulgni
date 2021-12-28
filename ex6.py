# if

temp = int(input("온도를 입력하세요"))

if 30<= temp:
    print("너무 더워요")
elif 10 <= temp and temp <= 30:
    print("괜찮은 날씨에요")
elif 0 <= temp <= 9:
    print("날씨가 추워요")
else:
    print("너무 추워요 나가지 마세요")


