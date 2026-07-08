import secrets
import string

print("=" * 50)
print("        RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("Enter password length (Minimum 8): "))

        if length < 8:
            print("Password length should be at least 8.\n")
            continue

        break

    except ValueError:
        print("Please enter a valid number.\n")

# Character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Ensure at least one character from each category
password = [
    secrets.choice(uppercase),
    secrets.choice(lowercase),
    secrets.choice(digits),
    secrets.choice(symbols)
]

# Remaining characters
all_characters = uppercase + lowercase + digits + symbols

for _ in range(length - 4):
    password.append(secrets.choice(all_characters))

# Shuffle password
secrets.SystemRandom().shuffle(password)

# Convert list to string
final_password = "".join(password)

print("\nGenerated Password:")
print(final_password)

print("\nPassword Length:", len(final_password))
print("Password generated successfully!")