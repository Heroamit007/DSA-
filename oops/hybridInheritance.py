class GrandParent:
    def show_grandparent(self):
        print("This is GrandParent class")

class Parent1(GrandParent):
    def show_parent1(self):
        print("This is Parent1 class")

class Parent2(GrandParent):
    def show_parent2(self):
        print("This is Parent2 class")

class Child(Parent1, Parent2):
    def show_child(self):
        print("This is Child class")

# Create object
obj = Child()
obj.show_grandparent()
obj.show_parent1()
obj.show_parent2()
obj.show_child()
