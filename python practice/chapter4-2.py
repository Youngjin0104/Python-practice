kor = int(input('국어 점수를 입력하세요 >>> '))
eng = int(input('영어 점수를 입력하세요 >>> '))
mat = int(input('수학 점수를 입력하세요 >>> '))

avg = (kor + eng + mat) / 3
msg = ''
if avg >= 80:
    msg = '합격'
else:
    msg = '불합격'

print(f'평균은 %.1f점이고, 결과는 {msg}입니다.' % avg)
