# SOLID
# DRY - Donot Repeat Yourself

class Emp:
    dept = "IT"
    company = "INFY"

    # Constructor - that construct an object
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
        self.empDetails = []
        self.empDetails.append([self.name, self.email, self.salary])

    def showCommonDetails(self):
        print(f"Company : {self.company}")
        print(f"Deparment : {self.dept}")

    def showEmp(self):
        print(f"Name is {self.name}")
        print(f"Email is {self.email}")
        print(f"Salary is {self.salary}")
        print("*" * 30)

    # Destructor - destroy an object
    def __del__(self):
        print(self.name, "object is destroyed")

emp_1 = Emp("John", "john12@gmail.com",45000.00)
emp_1.showCommonDetails()
emp_1.showEmp()

# print(emp_1.name, emp_1.email, emp_1.salary)
print(emp_1.empDetails)

del emp_1

emp_2 = Emp("Sam", "sam121@gmail.com",50000.00)
emp_2.showCommonDetails()
emp_2.showEmp()

print(emp_2.empDetails)
