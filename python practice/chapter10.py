while True:
    number = input('사업자 번호를 입력하세요 >>> ')
    num = number.replace('-','')
    if len(number) == 12:
        if number.find('-') == 3 and number.find('-',4) == 6:   
            if num.isdecimal() == True:
                print('올바른 형식 입니다.')
                print(number)
                break
            else:
                print('올바른 형식이 아닙니다.(2)')
                continue
        else:
            print('올바른 형식이 아닙니다.(1)')
            continue
    else:
        print('올바른 형식이 아닙니다.')
        continue


    
