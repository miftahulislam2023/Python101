class Marks:
    bangla = 10
    english = 30
    arabic = 50
    total = bangla + english + arabic
    """ def __init__(self, bangla, english, arabic):
        self.bangla = bangla
        self.english = english
        self.arabic = arabic
        self.total = bangla + english + arabic """
    def showMark(self):
        print(self.total)       

m1 = Marks()
m2 = Marks()

m1.showMark()
m2.showMark()