# Setting up properties for specific objects separately
class person:
    def welcome(self):
        print("Hello welcome to python learning")

    def hello_world(self):
        print("hello world")

    def sum(self, num1, num2):
        print(num1 + num2)


obj1 = person()
obj1.name = "Pritam"
obj1.phone = 9718374342
obj1.height = 9

obj2 = person()
obj2.name = "Saman"
obj2.phone = 80808080
obj2.weight = 70

print(obj1.height)
print(obj2.weight)

print(obj1)
