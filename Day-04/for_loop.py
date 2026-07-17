
# ====================================
# Topic : For Loop
# Author: Bayant Kaur
# Day   : 04
# ====================================

# Print numbers from 1 to 10
print("Print numbers from 1 to 10")
for i in range(1, 11):
    print(i)

# Print even numbers from 1 to 20
print("\nEven numbers from 1 to 20")
for i in range(2, 21, 2):
    print(i)

# Print odd numbers from 1 to 20
print("\nOdd numbers from 1 to 20")
for i in range(1, 21, 2):
    print(i)

# Print squares from 1 to 5
print("\nSquares from 1 to 5")
for i in range(1, 6):
    print(i * i)

# Table of 7
print("\nTable of 7")
num = 7
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

# Sum of numbers from 1 to 100
print("\nSum of numbers from 1 to 100")
total_sum = 0
for i in range(1, 101):
    total_sum = total_sum + i
print(total_sum)

# Sum of even numbers from 1 to 20
print("\nSum of even numbers from 1 to 20")
total_sum = 0
for i in range(2, 21, 2):
    total_sum = total_sum + i
print(total_sum)

# Count even numbers from 1 to 20
print("\nCount of even numbers from 1 to 20")
count = 0
for i in range(2, 21, 2):
    count = count + 1
print(count)

# Factorial of 5
print("\nFactorial of 5")
fact = 1
for i in range(1, 6):
    fact = fact * i
print(fact)

# Fizz (Divisible by 3)
print("\nFizz Program")
for i in range(1, 21):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# Reverse table of 8
print("\nReverse Table of 8")
num = 8
for i in range(10, 0, -1):
    print(f"{num} X {i} = {num * i}")
