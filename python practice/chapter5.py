carNumber = input('차량번호를 입력하세요 >>> ')

i = int(carNumber[-1])

if i%2 == 0:
    print(f'차량번호 \'{carNumber}\'는 오늘 운행가능입니다.')
else:
    print(f'차량번호 \'{carNumber}\'는 오늘 운행불가입니다.')
