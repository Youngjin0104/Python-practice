num = int(input('4자리 사원번호를 입력하세요 >>> '))

if num % 10 >= 5:
    result = '오전'
else :
    result = '오후'

print(f'근무시간은 {result}입니다.')
