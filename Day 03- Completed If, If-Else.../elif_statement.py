# =====================================
# Topic: Elif Statement
# Author: Bayant Kaur
# Day: 03
# =====================================

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


temp = int(input("Enter today's temperature: "))

if temp >= 40:
    print("Too Hot")
elif temp >= 25:
    print("Pleasant Weather")
else:
    print("Cold Weather")
