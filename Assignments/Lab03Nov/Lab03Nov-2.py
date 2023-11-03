class Person:
    name = None
    age = None
    address = None


person1_name = input("Enter the name of the first person: ")
person1_age = input("Enter the age of the first person: ")
person1_address = input("Enter the address of the first person: ")

person1 = Person()
person1.name = person1_name
person1.age = person1_age
person1.address = person1_address

person2_name = input("Enter the name of the second person: ")
person2_age = input("Enter the age of the second person: ")
person2_address = input("Enter the address of the second person: ")


person2 = Person()
person2.name = person2_name
person2.age = person2_age
person2.address = person2_address

# Print the details of the two persons
print("\nDetails of the first person:")
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
print(f"Address: {person1.address}")

print("\nDetails of the second person:")
print(f"Name: {person2.name}")
print(f"Age: {person2.age}")
print(f"Address: {person2.address}")
