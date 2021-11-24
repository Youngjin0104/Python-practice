class Person:

    cnt = 0

    def __init__(self,name):
        self.name = name
        print(f'{name} is born')
        Person.cnt += 1

    @classmethod
    def get_population(cls):
        return cls.cnt

    def __del__(self):
        print(f'{self.name} is dead')
        Person.cnt -= 1

man = Person('james')
woman = Person('emily')

print(f'전체 인구수: {Person.get_population()}명')

del man

print(f'전체 인구수: {Person.get_population()}명')
