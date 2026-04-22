# script to generate random password using bulit-in random and string modules
import random
import string

# define function called generate_password with length 12 set as default
def generate_password(length= 12): # combines all possible characters into one variable using (ascii_letters, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation # picks a random character from the pool of characters and repeats the process using a for loop 'length' of times and joins the characters into one string password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password())