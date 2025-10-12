class GrandFather:
    def home(self):
        print("Grandfather's house")

class Father(GrandFather):
    def car(self):
        print("Father's car")

class Son(Father):
    def bike(self):
        print("Son's bike")

s = Son()
s.home()
s.car()
s.bike()
