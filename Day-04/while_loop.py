
# ====================================
# Topic : While Loop
# Author: Bayant Kaur
# Day   : 04
# ====================================

# Print numbers from 1 to 10
print("Print numbers from 1 to 10")
i = 1
while i <= 10:
    print(i)
    i = i + 1

# Print even numbers from 1 to 20
print("\nEven numbers from 1 to 20")
i = 2
while i <= 20:
    print(i)
    i = i + 2

# Print odd numbers from 1 to 20
print("\nOdd numbers from 1 to 20")
i = 1
while i <= 20:
    print(i)
    i = i + 2

# Print squares from 1 to 5
print("\nSquares from 1 to 5")
i = 1
while i <= 5:
    print(i * i)
    i = i + 1

# Print cubes from 1 to 5
print("\nCubes from 1 to 5")
i = 1
while i <= 5:
    print(i * i * i)
    i = i + 1

# Table of 7
print("\nTable of 7")
num = 7
i = 1
while i <= 10:
    print(f"{num} X {i} = {num * i}")
    i = i + 1

# Sum of numbers from 1 to 100
print("\nSum of numbers from 1 to 100")
i = 1
total_sum = 0
while i <= 100:
    total_sum = total_sum + i
    i = i + 1
print(total_sum)

# Sum of even numbers from 1 to 20
print("\nSum of even numbers from 1 to 20")
i = 2
total_sum = 0
while i <= 20:
    total_sum = total_sum + i
    i = i + 2
print(total_sum)

# Count even numbers from 1 to 20
print("\nCount of even numbers from 1 to 20")
i = 2
count = 0
while i <= 20:
    count = count + 1
    i = i + 2
print(count)

# Factorial of 6
print("\nFactorial of 6")
fact = 1
i = 1
while i <= 6:
    fact = fact * i
    i = i + 1
print(fact)

# Fizz Program
print("\nFizz Program")
i = 1
while i <= 20:
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i = i + 1

# Reverse Table of 8
print("\nReverse Table of 8")
num = 8
i = 10
while i >= 1:
    print(f"{num} X {i} = {num * i}")
    i = i - 1

# Print odd numbers from 19 to 1
print("\nOdd numbers from 19 to 1")
i = 19
while i >= 1:
    print(i)
    i = i - 2
