# find the smallest number from a list

list1 = [10,15,5,50,100,90,34,560]

smallest = list1[0]

for x in list1:

    if x < smallest :
        smallest=x
    else:
        pass
print(f"smallest number in list is {smallest}")

list2=list1.copy()
list2.sort()
print(f"smallest number in list using direct methods is {list2[0]}")
print("Smallest element is:", min(list1))