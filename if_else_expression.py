#If Else Expression

a,b,c = 20,34,124

'''
if a > b:
    print("A is greatest")
else:
    print("B is greatest")
'''

'''
output = "A" if a > b else "B"
print(output,"is greatest...")
'''

output = "A" if a > b and a > c else "B" if b > a and b > c else "C"
print(output,"is greatest...")












