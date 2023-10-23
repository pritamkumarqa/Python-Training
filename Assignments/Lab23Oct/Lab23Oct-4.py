def doubling(x):
    return x * 2


output = doubling(5)
print(output)

newdoubling = lambda x: x * 2  # you can compare this to traditional function doubling created in top

newout = newdoubling(10)
print(newout)

# create a lambda expression to triple a number for eg: triple of 5 is 5*3 = 15

tripling = lambda x: x * 3
output = tripling(10)
print("Triple of a number is", output)
