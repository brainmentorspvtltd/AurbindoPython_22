# SOLID
# DRY - Donot Repeat Yourself

class Emp:
    name = None
    email = None
    dept = "IT"
    salary = 0.0
    company = "INFY"
    empDetails = []

    def takeInput(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
        self.empDetails.append([self.name, self.email, self.salary])

    def showCommonDetails(self):
        print(f"Company : {self.company}")
        print(f"Deparment : {self.dept}")

    def showEmp(self):
        print(f"Name is {self.name}")
        print(f"Email is {self.email}")
        print(f"Salary is {self.salary}")
        print("*" * 30)

emp_1 = Emp()
# emp_1.name = "John"
# emp_1.email = "john12@gmail.com"
# emp_1.salary = 45000.00
emp_1.takeInput("John", "john12@gmail.com",45000.00)
emp_1.showCommonDetails()
emp_1.showEmp()

# print(emp_1.name, emp_1.email, emp_1.salary)
print(emp_1.empDetails)

# print(f"Name is {emp_1.name}")
# print(f"Email is {emp_1.email}")
# print(f"Salary is {emp_1.salary}")

emp_2 = Emp()
# emp_2.name = "Sam"
# emp_2.email = "sam121@gmail.com"
# emp_2.salary = 50000.00
emp_2.takeInput("Sam", "sam121@gmail.com",50000.00)
emp_2.showCommonDetails()
emp_2.showEmp()

print(emp_2.empDetails)

# print(f"Name is {emp_2.name}")
# print(f"Email is {emp_2.email}")
# print(f"Salary is {emp_2.salary}")