# ===================================
# Topic : List Practice Questions
# Author: Bayant Kaur
# Day   : 06
# ===================================


# Question 1: Find Maximum Element
numbers = [12, 45, 7, 89, 23]

print(max(numbers))


# Question 2: Find Minimum Element
numbers = [12, 45, 7, 89, 23]

print(min(numbers))


# Question 3: Find Sum of All Elements
numbers = [12, 45, 7, 89, 23]

print(sum(numbers))


# Question 4: Count Even Numbers
numbers = [12, 45, 7, 89, 23]

count = 0

for i in numbers:
    if i % 2 == 0:
        count = count + 1

print("Even Numbers =", count)


# Question 5: Count Odd Numbers
numbers = [12, 45, 7, 89, 23]

count = 0

for i in numbers:
    if i % 2 != 0:
        count = count + 1

print("Odd Numbers =", count)


# Question 6: Search an Element
numbers = [12, 45, 7, 89, 23]

search = 89
found = False

for i in numbers:
    if i == search:
        found = True

if found:
    print("Found")
else:
    print("Not Found")


# Question 7: Reverse a List using Slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])


# Question 8: Find Second Largest Element
numbers = [12, 45, 7, 89, 23]

numbers.sort()

print("Second Largest =", numbers[-2])


# Question 9: Count Positive and Negative Numbers
numbers = [5, -3, 8, -1, 0, 9, -7]

positive = 0
negative = 0

for i in numbers:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1

print("Positive =", positive)
print("Negative =", negative)
