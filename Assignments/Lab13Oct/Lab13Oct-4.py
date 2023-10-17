# Write a program to find out the maximum of three numbers using ternary operator

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))
max = num1 if (num1 > num2 and num1 > num3) else num2 if num2 > num3 else num3
print("maximum if three numbers is ",max)
