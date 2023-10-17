s1 = float(input("Enter the side1 of Triangle \n"))
s2 = float(input("Enter the side2 of Triangle \n"))
s3 = float(input("Enter the side3 of Triangle \n"))

if s1==s2==s3:
    triangle_type = "Equilateral"
elif s1!=s2!=s3:
    triangle_type = "scalene"
else:
    triangle_type = "isosceles"

print(f"Trinage is of type {triangle_type}")