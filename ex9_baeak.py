# continue

absent = [2, 5] # 결석
no_book = [7] # 책을 안가져옴
for student in range (1, 11): # 1 ~ 10 변수 생성
    if student in absent: # absent 에 포함된 변수가 나오는지 확인
        continue
    elif student in no_book: # 만약 no_book 변수를 만나면 아래를 실행후
        print("오늘 수업은 여기까지!. {0}은 교무실로 ".format(student))
        break # 더이상 진행하지않고 멈춘다
    print("{}, 책을 읽어봐".format(student))