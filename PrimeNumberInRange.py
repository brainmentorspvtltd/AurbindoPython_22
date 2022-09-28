min_range = int(input("Enter min range : "))
max_range = int(input("Enter max range : "))

for num in range(min_range, max_range):
    for i in range(2,num//2):
        if num % i == 0:
            # print("Number is not prime...")
            break
    else:
        print(f"{num} is prime...")

