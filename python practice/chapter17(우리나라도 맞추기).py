class Quiz:

    answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']

    @classmethod
    def challenge(cls):
        try:
            user_answer = input('정답은? >>> ')
            if user_answer in cls.answer:
                cls.answer.pop(cls.answer.index(user_answer))
            else:
                raise Exception('틀렸습니다.')
        except Exception as e:
            print(e)
            Quiz.challenge()
        else:
            if len(cls.answer) == 0:
                print('모든 도를 맞췄습니다. 성공입니다.')
            else:
                print('정답입니다.')
                print(cls.answer)
                Quiz.challenge()

try:
    print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
    Quiz.challenge()
except Exception as e:
    print(e)
