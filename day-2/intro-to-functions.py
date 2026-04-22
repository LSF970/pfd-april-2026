# Functions

# def function_name(parameters):
#     # indented block of code
#     return something # optional

def add(num1, num2):
    return num1 + num2

print(add(5, 10)) # should output 15
print(add(10, 10)) # should output 20
print(add(100, 54)) # should output 154

def add_and_print(a, b):
    print(a + b)

def add_and_return(a, b):
    return a + b

result_1 = add_and_print(2, 3)
print("result1 is: ", result_1)

result_2 = add_and_return(2, 3)
print("result2 is", result_2)

# Simple examples

def tripler(num):
    return num * 3

print(tripler(3))
print(tripler(10))
print(tripler(99))

def greet(name):
    return f"Hello, {name}"

print(greet("Luke"))
print(greet("Mario"))

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(4))
print(is_even(7))
