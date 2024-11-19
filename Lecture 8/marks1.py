class Marks:
    def __init__(self, bangla, english, arabic):
        self.bangla = bangla
        self.english = english
        self.arabic = arabic
        self.total = bangla + english + arabic
    def showMark(self):
        print(self.total)       

m1 = Marks(78, 56, 89)
m2 = Marks(97, 78, 65)

m1.showMark()
m2.showMark()