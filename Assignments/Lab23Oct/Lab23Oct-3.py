# create a function with parameter which can do x^y

def x_power_y(x, y):
    return x ** y


output = x_power_y(6, 2)
print(output)

out = lambda x,y:x**y
print(out(5,3))