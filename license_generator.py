import random
import string

def generate_license_key():
    # Generate a license key in the format "XXX-XXX-XXX"
    segments = []
    for _ in range(3):
        segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        segments.append(segment)
    return '-'.join(segments)

def generate_software_id():
    # Generate a software ID in the format "SOFTWARE1", "SOFTWARE2", etc.
    base_id = "SOFTWARE"
    number = random.randint(1, 1000)  # Random number between 1 and 1000
    return f"{base_id}{number}"

def generate_user_id():
    # Generate a user ID in the format "USER1", "USER2", etc.
    base_id = "USER"
    number = random.randint(1, 1000)  # Random number between 1 and 1000
    return f"{base_id}{number}"

# Generate and print values
license_key = generate_license_key()
software_id = generate_software_id()
user_id = generate_user_id()

print(f"Generated License Key: {license_key}")
print(f"Generated Software ID: {software_id}")
print(f"Generated User ID: {user_id}")
