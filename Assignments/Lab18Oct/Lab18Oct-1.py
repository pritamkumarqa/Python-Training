# Find the factorial of a integer given the input by user
num1 = int(input("Enter the number \n"))
y = num1
list1=[]
for x in range(y,0,-1):
    list1.append(x)
print(list1)
fact=1
for x in list1:
    fact=fact*x
print(f"factorial of {num1} is {fact}")