import random
import string

def generate_password(length):
    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input
length = int(input("Enter the desired password length: "))
password = generate_password(length)
print("Generated Password:", password)
