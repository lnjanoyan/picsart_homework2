class Publication:
    def __init__(self, title: str, price: int):
        self.title = title
        self.price = price


class Book(Publication):
    def __init__(self, title: str, price: int, count_of_page: int):
        super().__init__(title, price)
        self.count_of_page = count_of_page

    def setData(self, count_of_page):
        self.count_of_page = count_of_page

    def getData(self, count_of_page):
        return self.count_of_page


class Tape(Publication):
    def __init__(self, title: str, price: int, playing_time: int):
        super().__init__(title, price)
        self.playing_time = playing_time

    def setData(self, playing_time):
        self.playing_time = playing_time

    def getData(self, playing_time):
        return self.playing_time


book1 = Book('title1', 2000, 90)
tape1 = Tape('tit1', 3000, 50)
book2 = Book('title2', 2000, 45)
tape2 = Tape('tit2', 4000, 75)
print(book1.getData(50), tape2.setData(20), tape2.playing_time)
