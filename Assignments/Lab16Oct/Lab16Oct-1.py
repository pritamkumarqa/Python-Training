score = float(input("Enter the score \n"))
if score >= 90 and score <= 100:
    Grade = "A"
elif score >= 80 and score <= 89:
    Grade = "B"
elif score >= 70 and score <= 79:
    Grade = "C"
elif score >= 60 and score <= 60:
    Grade = "D"
elif score >= 0 and score <= 59:
    Grade = "F"
else:
    Grade = "Invalid Score"
print(f"your Garde is {Grade} ")

