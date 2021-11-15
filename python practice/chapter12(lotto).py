import random
import time

pot = list(range(1,46))
jackpot = []
for i in range(6):
    random.shuffle(pot)
    jackpot.append(pot[-1])   
    print(f'{i + 1}번째 당첨번호는 {jackpot[i]}입니다.')
    time.sleep(2)

jackpot.sort()

print(f'이번 당첨번호는 {jackpot}입니다.')

