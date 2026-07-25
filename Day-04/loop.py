# ====================================
# Topic : Break and Continue
# Author: Bayant Kaur
# Day   : 04
# ====================================


# Break Statement
# Stops the loop when the condition becomes true

print("\nBreak Statement")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Break with Even Number
print("\nBreak at First Even Number")
for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i)

# Break with Sum
print("\nBreak when Sum Reaches 30")
total = 0
for i in range(1, 100):
    total = total + i
    if total >= 30:
        break
print(total)


# Continue Statement
# Skips the current iteration and moves to the next iteration

print("\nContinue Statement")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Skip Even Numbers
print("\nSkip Even Numbers")
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)

# Skip Multiples of 5
print("\nSkip Multiples of 5")
for i in range(1, 30):
    if i % 5 == 0:
        continue
    print(i)

# Continue with Nested Loop
print("\nNested Loop with Continue")
for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            continue
        print(j, end=" ")
    print()

# Skip a Complete Row using Continue
print("\nSkip Third Row")
for i in range(1, 6):
    if i == 3:
        continue

    for j in range(1, i + 1):
        print("*", end=" ")
    print()
