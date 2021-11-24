class Car:

    max_oil = 50

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f'현재 주유상태 : {self.oil}')

class Hybrid(Car):

    max_charge = 30
    
    def __init__(self, oil, car_charge):
        super().__init__(oil)
        self.car_charge = car_charge

    def charge(self, car_charge):
        if car_charge <= 0:
            return
        self.car_charge += car_charge
        if self.car_charge > Hybrid.max_charge:
            self.car_charge = Hybrid.max_charge

    def hybrid_info(self):
        print(f'현재 주유상태 : {self.oil}')
        print(f'현재 충전상태 : {self.car_charge}')
            
        
car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()
