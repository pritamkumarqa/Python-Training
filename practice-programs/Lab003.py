class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"I am {self.name} and my age is {self.age} year old")

    def __str__(self):
        return (f"I am {self.name} and my age is {self.age}")

class Men(Person):
    pass

obj1 = Men('Pritam', 30)
print(obj1)
obj1.hello()

