# Password Generator

import random
import string

print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

include_letters = input("Include letters? (yes/no): ").lower()
include_numbers = input("Include numbers? (yes/no): ").lower()
include_symbols = input("Include symbols? (yes/no): ").lower()

characters = ""

# Adding letters
if include_letters == "yes":
    characters += string.ascii_letters   # a-z and A-Z

# Adding numbers
if include_numbers == "yes":
    characters += string.digits          # 0-9

# Adding symbols
if include_symbols == "yes":
    characters += string.punctuation     # !@#$%^&* etc.

if characters == "":
    print("Error: You must select at least one character type.")
else:
    # Generate password
    password = ""
    for i in range(length):
        password += random.choice(characters)

    # Display result
    print("\nGenerated Password:")
    print(password)
