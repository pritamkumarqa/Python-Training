# Write a program to calculate the sum of digits of integer number. For eg: sum of 234 = 9
num1 = input("Enter the number :  ")
total = 0
for x in num1:
    total = total + int(x)
print("Sum of digits is : ", total)

