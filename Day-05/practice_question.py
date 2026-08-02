# =====================================
# Topic : Function Practice Questions
# Author: Bayant Kaur
# Day   : 05
# =====================================


# -----------------------------------
# 1. Calculator Function
# -----------------------------------

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    elif op == "%":
        return a % b
    else:
        return "Invalid Operator"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))
print(calculator(17, 5, "%"))


# -----------------------------------
# 2. Reverse a String
# -----------------------------------

def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))


# -----------------------------------
# 3. Find Smallest Number
# -----------------------------------

def smallest(a, b, c):
    return min(a, b, c)

print(smallest(12, 5, 18))


# -----------------------------------
# 4. Find Largest Number
# -----------------------------------

def largest(a, b, c):
    return max(a, b, c)

print(largest(12, 5, 18))


# -----------------------------------
# 5. Find Length of String
# -----------------------------------

def length(text):
    return len(text)

print(length("Python"))


# -----------------------------------
# 6. Check Even or Odd
# -----------------------------------

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(24))


# -----------------------------------
# 7. Check Positive or Not
# -----------------------------------

def is_positive(num):
    if num > 0:
        return "Positive"
    else:
        return "Not Positive"

print(is_positive(-3))


# -----------------------------------
# 8. Percentage Calculator
# -----------------------------------

def percentage(obtained, total):
    return (obtained / total) * 100

print(percentage(450, 500))


# -----------------------------------
# 9. Count Vowels
# -----------------------------------

def count_vowels(text):
    text = text.lower()
    count = 0

    for ch in text:
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("Bayant Kaur"))


# -----------------------------------
# 10. Count Letters
# -----------------------------------

def count_letters(text):
    text = text.lower()
    count = 0

    for ch in text:
        if ch in "abcdefghijklmnopqrstuvwxyz":
            count += 1

    return count

print(count_letters("Bayant Kaur 123"))


# -----------------------------------
# 11. Check Adult
# -----------------------------------

def is_adult(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(is_adult(20))


# -----------------------------------
# 12. Find Grade
# -----------------------------------

def find_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print(find_grade(82))
