
dict1 = dict(name="Aman",nam2="Sonu")
print(dict1)
dict2={1:"Pritam",2:"Kumar",3:"Parashar","training":"python"}
print(dict2)
print(dict2[3])
print(dict2.get(2))
print(dict2.get('2'))
#print(dict2['2'])
print(dict2[2])
dict2.popitem()
for x in dict2:
    print(dict2[x])

def is_even(x):
    return x%2==0
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(map(is_even,list1))
list3=list(filter(is_even,list1))
print(list2)
print(list3)
list4=[]
for x in list1:
    if x%2==0:
        list4.append(x)
    else:
        pass
print(list4)
