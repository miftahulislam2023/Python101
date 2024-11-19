class Student: #student model
    def __init__(self, n, r, sname):
        self.name = n
        self.roll = r
        self.schoolName = sname
    def show(self):
        print(self.name, self.roll, self.schoolName)

s1 = Student("Zadu", 10, "Zadu high school")
s2 = Student("Kadu", 3, "harpic high school")

s1.show()
s2.show()
#Polymorphism, encapsulation, inheritance, abstarction

#step 1: model making
#step 2: creating something out of the model