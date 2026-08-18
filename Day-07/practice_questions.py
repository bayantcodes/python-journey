# ===================================
# Topic : Tuple Practice Questions
# Author: Bayant Kaur
# Day   : 07
# ===================================


# Q1. Create a tuple of 5 numbers and print the first
# and last element.

numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[-1])


# Q2. Print the last two elements of a tuple using slicing.

numbers = (10, 20, 30, 40, 50)

print(numbers[-2:])


# Q3. Reverse a tuple using slicing.

numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])


# Q4. Count the occurrence of an element using count().

numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))


# Q5. Find the first index of an element using index().

numbers = (10, 20, 30, 40, 20)

print(numbers.index(20))


# Q6. Count the number of even elements in a tuple.

numbers = (10, 25, 30, 45, 50)

count = 0

for i in numbers:
    if i % 2 == 0:
        count += 1

print("Even Numbers =", count)


# Q7. Find the sum of all odd elements in a tuple.

numbers = (10, 25, 30, 45, 50)

total = 0

for i in numbers:
    if i % 2 != 0:
        total += i

print("Sum of Odd Numbers =", total)


# Q8. Search for an element in a tuple without using
# the 'in' operator.

numbers = (12, 45, 7, 89, 23)

search = 89
found = False

for i in numbers:
    if i == search:
        found = True

if found:
    print("Found")
else:
    print("Not Found")


# Q9. Try to modify an element of a tuple.

numbers = (10, 20, 30)

# numbers[1] = 50
# This gives TypeError because tuples are immutable.


# Q10. Add a new element to a tuple by converting it
# into a list first.

numbers = (10, 20, 30, 40, 50)

numbers_list = list(numbers)
numbers_list.append(60)

numbers = tuple(numbers_list)

print(numbers)
