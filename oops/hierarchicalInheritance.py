class Parent:
    def show(self):
        print("This is Parent class")

class Child1(Parent):
    def feature1(self):
        print("This is Child1 class")

class Child2(Parent):
    def feature2(self):
        print("This is Child2 class")

# Create objects
c1 = Child1()
c2 = Child2()

c1.show()
c1.feature1()

c2.show()
c2.feature2()
