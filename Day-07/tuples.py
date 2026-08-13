# ===================================
# Topic : Tuples
# Author: Bayant Kaur
# Day   : 07
# ===================================


# Creating a Tuple
numbers = (10, 20, 30, 40, 50)
print(numbers)


# Tuple with Different Data Types
student = ("Bayant", 20, 47.5, True)
print(student)


# Empty Tuple
empty = ()
print(empty)


# Single Element Tuple
single = (10,)
print(single)


# Accessing Elements using Indexing
print(numbers[0])
print(numbers[2])


# Negative Indexing
print(numbers[-1])
print(numbers[-2])


# Tuple Slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[-2:])


# Reverse Tuple using Slicing
print(numbers[::-1])


# Length of Tuple
print(len(numbers))


# Checking an Element
print(30 in numbers)
print(100 in numbers)


# Looping through a Tuple
for i in numbers:
    print(i)


# Nested Tuple
nested = ((1, 2, 3), (4, 5, 6))
print(nested)
print(nested[0])
print(nested[0][1])
