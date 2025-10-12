class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary = salary
    def calculate_bonus(self):
        return self.salary * 0.10
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.25

e = Employee("raj", 8000)
m = Manager("Amit", 100000)

print(e.calculate_bonus())
print(m.calculate_bonus())
