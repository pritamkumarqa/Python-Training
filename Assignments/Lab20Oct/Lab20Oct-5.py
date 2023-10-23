# Write a program to calculate the sum of digits of integer number. For eg: sum of 234 = 9
#num1 = int(input("Enter the number :  "))
num1=1265
total = 0
while num1 > 0:
    r = num1%10
    total = total+r
    num1 = num1//10
print(total)
