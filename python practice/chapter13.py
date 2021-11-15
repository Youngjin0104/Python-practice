with open('연락처.txt','rt',encoding ='UTF-8') as file:

    line_list = file.readlines()
    cnt = 0

    for line in line_list:
        if line.count('011'):
            cnt += 1
        print(line)
    print(f'총 {cnt}건의 011 데이터를 찾았습니다.')

with open('연락처.txt','wt',encoding ='UTF-8') as file:
    
    for line in line_list:
        line = line.replace('011','010')
        print(line)
        file.write(line)
    print('모든 데이터를 수정했습니다.')
