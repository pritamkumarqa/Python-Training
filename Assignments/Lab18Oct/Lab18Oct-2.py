# Find the factorial of a integer given the input by user
num1 = int(input("Enter the number till where fibonacci series to be printed \n"))
a = 0
b = 1
list1 = []
list1.append(a)
list1.append(b)
n=a+b

for i in range(1, num1+1):
    c=a+b
    if c > num1:
        break
    list1.append(c)
    a=b
    b=c
print(list1)
