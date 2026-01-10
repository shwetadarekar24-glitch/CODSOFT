This Python program generates a strong random password by taking the desired length from the user, combining letters, numbers, and symbols, and displaying the generated password on the screen

import random
import string

# User input for password length
length = int(input("Enter desired password length: "))

# Characters for password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display password
print("Generated Password:", password)
