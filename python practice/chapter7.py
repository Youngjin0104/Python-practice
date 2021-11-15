exam = [99, 78, 100, 81, 54, 100, 71, 80]
score = []
for i in exam:
    i += 5
    if i > 100:
        i = 100
    score.append(i)
print(score)
