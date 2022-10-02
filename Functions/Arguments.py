# Default arguments
def add(x=0,y=0):
    z = x + y
    print("Sum is",z)

# Positional Arguments
add(4,5)
add(6,8)
add(12,45)

# Keywords arguments
add(x = 12, y = 30)
add(y = 10, x = 5)

add()       # will pass 0 to x and y
add(5)      # will pass 5 to x and y will be 0
add(y=12)   # x will be 0 and y will be 12

