# =====================================
# Topic : Function Arguments
# Author: Bayant Kaur
# Day   : 05
# =====================================


# -----------------------------------
# 1. Required Arguments
# -----------------------------------

def greet(name):
    print("Hello", name)

greet("Bayant")


# -----------------------------------
# 2. Keyword Arguments
# -----------------------------------

def student(name, age):
    print("Name:", name)
    print("Age :", age)

student(age=20, name="Bayant")


# -----------------------------------
# 3. Default Arguments
# -----------------------------------

def country(name, country="India"):
    print(name, "is from", country)

country("Bayant")
country("John", "USA")


# -----------------------------------
# 4. Variable Length Arguments (*args)
# -----------------------------------

def total(*args):
    print(args)

total(10, 20, 30)
total(5, 8)


# -----------------------------------
# 5. Variable Length Arguments Example
# -----------------------------------

def maximum(*args):
    print(max(args))

maximum(45, 12, 78, 3, 29)


# -----------------------------------
# 6. Arbitrary Keyword Arguments (**kwargs)
# -----------------------------------

def details(**kwargs):
    print(kwargs)

details(name="Bayant", age=20, branch="AIML")


# -----------------------------------
# 7. **kwargs Example
# -----------------------------------

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Bayant", age=20, college="CGC Landran")
