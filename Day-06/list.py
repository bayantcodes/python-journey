# ===================================
# Topic : Lists
# Author: Bayant Kaur
# Day   : 06
# ===================================


# Creating a List
fruits = ["Apple", "Banana", "Mango", "Grapes"]
print(fruits)


# Accessing Elements using Indexing
print(fruits[0])
print(fruits[1])


# Negative Indexing
print(fruits[-1])
print(fruits[-2])


# List Slicing
print(fruits[0:2])
print(fruits[1:])
print(fruits[:3])
print(fruits[-2:])


# Reverse List using Slicing
print(fruits[::-1])


# Updating List Elements
fruits[1] = "Orange"
print(fruits)


# List with Different Data Types
student = ["Bayant", 20, 47.5, True]
print(student)


# Finding Length of a List
print(len(fruits))


# Checking an Element in a List
print("Mango" in fruits)
print("Apple" not in fruits)


# Looping through a List
for fruit in fruits:
    print(fruit)


# Nested List
numbers = [[1, 2, 3], [4, 5, 6]]
print(numbers)
print(numbers[0])
print(numbers[0][1])
