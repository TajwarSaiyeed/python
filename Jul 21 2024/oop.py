class Employee:
    # salary = 89
    # name = None
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        print(self.salary)


rohan = Employee("rohan", 89)
abid = Employee("Abid", 4855425)

# print(rohan.name, abid.name)
# abid.get_salary()
