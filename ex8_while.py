# while

customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비 되었습니다. {1}번 남았어요. " .format(customer, index)) #{} 안에 숫자를 기입하지 않으면 순서대로 함수를 불러온다
    index -= 1
    if index == 0:
        print("커피가 폐기 처분되었습니다")


guest = "토르"
person = "Unknown"

while person != customer:
    print("{}, 커피가 준비 되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요?")
    if person == customer:
        print("맛있게 드시길 바랍니다.")

