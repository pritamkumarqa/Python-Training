name = "hello world"
print(name.capitalize())

print(name.title())

# Take 5 numbers from user and add duplicate and then print the non duplicate numbers

# str1 = input("Enter numbers separated by space \n")
# print(str1)
# list1 = str1.split(" ")
# print(list1)

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
num4 = int(input("Enter 4th number : "))
num5 = int(input("Enter 5th number : "))
num6 = int(input("Enter 6th number : "))

list1 = [num1,num2,num3,num4,num5,num6]
print(list1)
set1 = {num1,num2,num3,num4,num5,num6}
print(set1)
set2 = set(list1)
print(set1)
