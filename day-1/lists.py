# Lists

# Lists are ordered, mutable, allows duplicate values

coaches_list = ["Callum", "Aidan", "Sandra", "Remi"]

print(len(coaches_list))

# Indexing
print(coaches_list[0])

# Up to 3rd element
print(coaches_list[:3])

# last 2 elements only
print(coaches_list[2:])

# check a value is in a list
print("Luke" in coaches_list)

# Change/overwrite a value in a list
coaches_list[1] = "Bob"

print(coaches_list)

# List methods

num_list = [1, 5, 6, 3, 75, 2]

# inserting into a list
num_list.insert(2, 450)
print(num_list)

# remove the first item in a list
num_list.pop(0)
print(num_list)

# removing the last item in a list
num_list.pop()
print(num_list)

# sorting a list
num_list.sort()
print(num_list)

# descending order
num_list.sort(reverse=True)
print(num_list)

# Arrays in Python are like lists but they can only contain numeric values
# They allow for more complex numeric operations/processing