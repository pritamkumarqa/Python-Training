y = int(input("Enter the year to be checked \n"))
# if (y%4 == 0):
#     if (y%100 !=0):
#         print(f"{y} is a leap year")
#     elif (y%100 == 0 and y%400 == 0):
#         print(f"{y} is a leap year")
#     else:
#         print(f"{y} is not a leap year")
# else:
#     print(f"{y} is not a leap year")

if (y%4 == 0 and y%100 != 0) or (y%4==0 and y%100==0 and y%400==0):
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")