# =====================================
# Topic: Nested If
# Author: Bayant Kaur
# Day: 03
# =====================================

pin = True
balance = 8000

if pin == True:
    print("PIN Verified")

    if balance >= 5000:
        print("Transaction Successful")


print("--------------------------")

age = 19
documents = True

if age >= 18:
    print("Age Verified")

    if documents == True:
        print("Admission Confirmed")
