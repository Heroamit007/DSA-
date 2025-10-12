class Father:
    def skill(self):
        print("Father: Knows driving.")

class Mother:
    def skill(self):
        print("Mother: Knows cooking.")

class Child(Mother,Father ):
    def hobby(self):
        print("Child: Loves painting.")

c = Child()
c.hobby()
c.skill()   # which one executes?
