# *args - variable length arguments
def add(*x):
    # print(x)
    s = 0
    for i in x:
        s += i
    print("Sum is",s)

# add(4)
# add(5,6)
# add(5,3,4,6)
# add(3,4,6,7,3,4,6,7)
# add(2,45,6,3)

# **kwargs - keyword argument
def person(**details):
    print(details)

person(name = "John")
person(id = 101, name = "Ram", age = 34)
person(id = 102, name = "Shyam", salary = 45000, age = 40, dept = "IT")



