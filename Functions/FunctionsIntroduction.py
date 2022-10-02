# Global
x = 23
y = 43
def calc():
    # Local variable
    # global x
    x = 2
    y = 6
    z = x + y
    print("Sum is",z)

calc()

z = x - y
print("Sub is",z)

