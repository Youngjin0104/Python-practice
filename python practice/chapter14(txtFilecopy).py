while True:
    userInput = input('복사할 파일명을 입력하세요 : ')

    with open(userInput, 'rb') as source:
        userInput1 = userInput.split('.')
        if userInput1[-1] != 'txt':
            print('복사할 수 없는 파일입니다.')
        else:
            with open('복사본-' + userInput, 'wb') as copy:
                buffer = source.readline()
                if not buffer:
                    break
                copy.write(buffer)
                print('복사본-' + source.name + '파일이 생성되었습니다.')
                break
