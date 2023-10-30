class person:
    def welcome(self):
        print("Hello welcome to python learning")

    def hello_world(self):
        print("hello world")
    def sum(self,num1,num2):
        print(num1+num2)


obj1 = person()
obj1.welcome()
person.welcome(obj1)    # this statement is equivilaent to above statement i.e obj1.welcome()

obj1.sum(12,13)

