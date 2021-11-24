class Watch:

    def watch(self):
        time1 = []
        time = input('시간을 입력하세요>>> ')
        time1 = time.split(':')
        self.hour = int(time1[0])
        self.minute = int(time1[1])
        self.second = int(time1[2])

    def add_hour(self):
        hour = int(input('계산할 시간을 입력하세요 >>> '))
        self.hour += hour

    def add_minute(self):
        minute = int(input('계산할 분을 입력하세요 >>> '))
        self.minute += minute

    def add_second(self):
        second = int(input('계산할 초를 입력하세요 >>> '))
        self.second += second

    def print_info(self):
        print(f'계산된 시간은 {self.hour%24 + self.minute//60}시 {self.minute%60 + self.second//60}분 {self.second%60}초 입니다.')
         
watch = Watch()
watch.watch()
watch.add_hour()
watch.add_minute()
watch.add_second()
watch.print_info()
