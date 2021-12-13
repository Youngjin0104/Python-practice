import random

class UpDown:

    def __init__(self):
        self.answer = random.randrange(1, 101)
        self.cnt = 1

    def challenge(self):
        
        try:
            user_input = int(input('입력(1 ~ 100) >>>'))
            if user_input < 1 or user_input > 100:
                raise TypeError('1 ~ 100 사이만 입력하세요')
        except TypeError as e:
            print(e)
            self.challenge()
        except Exception:
            print('1 ~ 100 사이의 숫자를 입력해주세요.')
            self.challenge()
        else:
            if user_input > self.answer:
                self.cnt += 1
                print('Down!')
                self.challenge()
            elif user_input < self.answer:
                self.cnt += 1
                print('UP!')
                self.challenge()
            else:
                print(f'{self.cnt}만의 정답입니다.')       

    def play(self):
        self.challenge()

game = UpDown()
game.play()
