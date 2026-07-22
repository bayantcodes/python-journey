# ====================================
# Topic : Star Patterns
# Author: Bayant Kaur
# Day   : 04
# ====================================

# Increasing Triangle
print("Increasing Triangle")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Decreasing Triangle
print("\nDecreasing Triangle")
for i in range(5):
    for j in range(5 - i):
        print("*", end="")
    print()

# Right Shift Triangle
print("\nRight Shift Triangle")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()

# Reverse Right Shift Triangle
print("\nReverse Right Shift Triangle")
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()

# Pyramid Pattern
print("\nPyramid Pattern")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Reverse Pyramid Pattern
print("\nReverse Pyramid Pattern")
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Butterfly Pattern
print("\nButterfly Pattern")

# Upper Half
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    for k in range(2 * (5 - i)):
        print(" ", end="")
    for l in range(1, i + 1):
        print("*", end="")
    print()

# Lower Half
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    for k in range(2 * (5 - i)):
        print(" ", end="")
    for l in range(1, i + 1):
        print("*", end="")
    print()
