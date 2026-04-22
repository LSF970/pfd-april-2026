# Dictionaries and Control Flow

def check_age(age):
    if age >= 18:
        return "You are an adult"
    elif age >= 13:
        return "You are a teenager"
    else:
        return "You are a child"

print(check_age(20))
print(check_age(12))
print(check_age(56))

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry denied.")

# Using 'or'
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Using 'not'
light_on = False
if not light_on:
    print("Turn on the light!")

# Loops - iterating over a sequence

# Loop through a list
fruits = ["apple", "pineapple", "banana"]

for fruit in fruits:
    print("I like ", fruit)

# loop with a range
for i in range(5):
    print(i)

# while loops - Repeat a block of code while a condition is True

num = 1

while num <= 5:
    print(num)
    num += 1


# break example
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#
# pass example
for i in range(3):
    pass  # placeholder

# Dictionaries - Key/Value pairs, mutable

# Create a dictionary(dict)
my_dictionary = {
    "first_name": "Joe",
    "last_name": "Bloggs",
    "address": "17 Pennsylvania Ave."
}

# Get a value using a key
print("My name is", my_dictionary["first_name"])

# Changing a value
my_dictionary["address"] = "123 Main St."

# Add key/value pair
my_dictionary["job"] = "Golfer"

# Print out all values
print(my_dictionary.values())

# Print out all keys
print(my_dictionary.keys())

# Use a for loop to print keys and values
for keys, values in my_dictionary.items():
    print(keys, values)

# deleting a key/value pair
del my_dictionary["first_name"]
for keys, values in my_dictionary.items():
    print(keys, values)

# Clear the dictionary completely
my_dictionary.clear()
print(my_dictionary)