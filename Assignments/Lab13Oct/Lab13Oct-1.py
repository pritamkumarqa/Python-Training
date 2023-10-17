# compare two numbers and find out which one is greater using ternary operator

a = int(input("Enter value of a\n"))
b = int(input("Enter value of b\n"))
result = "equal to" if a == b else "greater than" if a > b else "less than"
print(f"{a} is {result} {b}")
