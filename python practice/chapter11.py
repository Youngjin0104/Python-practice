total = 0
def gift(dic, who, money):
    dic[who] = money
    global total
    total = sum(dic.values())

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
print(f'축의금 명단 : {wedding}')
print(f'전체 축의금 : {total}')
