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

ch = input("Enter your choice : ")
fnum = int(input("Enter first num : "))
snum = int(input("Enter second num : "))

if ch == "1":
    res = add(fnum, snum)
elif ch == "2":
    res = sub(fnum, snum)
elif ch == "3":
    res = div(fnum, snum)
elif ch == "4":
    res = mul(fnum, snum)
else:
    res = 0
    print("Invalid choice...")

print("Result is",res)

