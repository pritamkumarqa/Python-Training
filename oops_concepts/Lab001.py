class person:
    def welcome(self):
        print("Hello welcome to python learning")

    def hello_world(self):
        print("hello world")


obj1 = person()
obj1.welcome()
obj1.hello_world()


def training():
    print("This is training program")


print(training)
print(obj1.welcome)
# print(welcome) ---> This statement will give error that welcome is not defined
training()
