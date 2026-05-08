# Password Generator in Python

import random
import string

print("=== Random Password Generator ===")

# Get password length from user
length = int(input("Enter password length: "))

# Character type options
include_letters = input("Include letters? (yes/no): ").lower()
include_numbers = input("Include numbers? (yes/no): ").lower()
include_symbols = input("Include symbols? (yes/no): ").lower()

# Store selected characters
characters = ""

# Add letters
if include_letters == "yes":
    characters += string.ascii_letters   # a-z and A-Z

# Add numbers
if include_numbers == "yes":
    characters += string.digits          # 0-9

# Add symbols
if include_symbols == "yes":
    characters += string.punctuation     # !@#$%^&* etc.

# Check if at least one option is selected
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