str1 = '"김철수",85'

str1 = str1.split(',')

name = str1[0].strip('"')
score = str1[1]

print(f'이름은 {name}이고, 점수는 {score}점 입니다')
