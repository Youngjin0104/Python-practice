class Song:

    def set_song(self, title, genre):
        self.title = title
        self.genre = genre

    def print_song(self):
        print(f'노래제목 : {self.title}({self.genre})')

class Singer:

    def set_singer(self, name):
        self.name = name

    def hit_song(self, song):
        self.song = song.print_song()
        
    def print_singer(self):
        print(f'가수이름: {self.name}')

song = Song()
singer = Singer()

song.set_song('취중진담', '발라드')
singer.set_singer('김동률')
singer.print_singer()
singer.hit_song(song)

