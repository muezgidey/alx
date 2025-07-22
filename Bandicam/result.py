score = int(input("Enter your result (0-100): "))

if score >= 90:
    grade = "A+"
elif score >= 85:
    grade = "A"
elif score >= 80:
    grade = "A-"
elif score >= 75:
    grade = "B+"
else:
    grade = "Failed"

print("Your grade is:", grade)
