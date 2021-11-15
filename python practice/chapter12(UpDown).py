import random
import math
from datetime import *

start = datetime.now()

print('Up Down game start')

result = random.randrange(1,100)

while True:
    userInput = int(input('어떤 값일까요 ? '))
    if result == userInput:
        print('정답입니다')
        end = datetime.now()
        correctAnswerTime = end - start
        cat = correctAnswerTime.total_seconds()
        time = math.trunc(cat)
        print(f'{time}초 만에 성공했습니다.')
        break
    elif result < userInput:
        print('Down')
    elif result > userInput:
        print('Up')
