print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')

exam = []
score = 1
while score > 0:
    score = int(input('점수 입력 >>> '))
    exam.append(score)

exam.pop()
print(f'평균 = {sum(exam)/len(exam):.1f}, 최대 = {max(exam)}, 최소 = {min(exam)}')
