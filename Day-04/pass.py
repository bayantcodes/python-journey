# ====================================
# Topic : Pass Statement
# Author: Bayant Kaur
# Day   : 04
# ====================================

# Pass Statement
# Does nothing and allows the program to continue normally

print("\nPass Statement")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)

# Pass with Even Numbers
print("\nPass with Even Numbers")
for i in range(1, 11):
    if i % 2 == 0:
        pass
    print(i)

# Pass with Nested Loop
print("\nPass with Nested Loop")
for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            pass
        print(j, end="")
    print()
