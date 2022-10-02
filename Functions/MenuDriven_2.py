def add(x,y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

def div(x,y):
    z = x / y
    return z

def mul(x,y):
    z = x * y
    return z

print("""
1. Addition
2. Subtraction
3. Division
4. Multiplication
""")

ch = int(input("Enter your choice : "))
fnum = int(input("Enter first num : "))
snum = int(input("Enter second num : "))

operations = [add, sub, div, mul]
res = operations[ch - 1](fnum, snum)
print("Result is",res)

