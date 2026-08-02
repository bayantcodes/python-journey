# =====================================
# Topic : Functions
# Author: Bayant Kaur
# Day   : 05
# =====================================

# Function to add two numbers
def add(a, b):
    return a + b

print("Addition:", add(10, 5))


# Function to subtract two numbers
def subtract(a, b):
    return a - b

print("Subtraction:", subtract(20, 8))


# Function to multiply two numbers
def multiply(a, b):
    return a * b

print("Multiplication:", multiply(6, 9))


# Function to divide two numbers
def divide(a, b):
    return a / b

print("Division:", divide(20, 4))


# Function to return full name
def full_name(first, last):
    return first + " " + last

print(full_name("Bayant", "Kaur"))


# Function to calculate total marks
def total_marks(m1, m2, m3):
    return m1 + m2 + m3

print("Total Marks:", total_marks(80, 75, 90))


# Function to find grade
def find_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print("Grade:", find_grade(82))


# Function to check adult
def is_adult(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(is_adult(20))


# Function to count vowels
def count_vowels(text):
    text = text.lower()
    count = 0

    for ch in text:
        if ch in "aeiou":
            count += 1

    return count

print("Vowels:", count_vowels("Bayant Kaur"))


# Function to count letters
def count_letters(text):
    text = text.lower()
    count = 0

    for ch in text:
        if ch in "abcdefghijklmnopqrstuvwxyz":
            count += 1

    return count

print("Letters:", count_letters("Bayant Kaur 123"))
