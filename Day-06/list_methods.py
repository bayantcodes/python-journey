# ===================================
# Topic : List Methods
# Author: Bayant Kaur
# Day   : 06
# ===================================


# 1. append()
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Grapes")
print(fruits)


# 2. insert()
fruits.insert(1, "Orange")
print(fruits)


# 3. extend()
more_fruits = ["Kiwi", "Papaya"]
fruits.extend(more_fruits)
print(fruits)


# 4. remove()
fruits.remove("Orange")
print(fruits)


# 5. pop()
fruits.pop()
print(fruits)


# 6. index()
print(fruits.index("Banana"))


# 7. count()
numbers = [10, 20, 10, 30, 10, 40]
print(numbers.count(10))


# 8. sort()
numbers.sort()
print(numbers)


# 9. reverse()
numbers.reverse()
print(numbers)


# 10. copy()
new_numbers = numbers.copy()
print(new_numbers)


# 11. clear()
new_numbers.clear()
print(new_numbers)
