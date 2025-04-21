import re
import getpass  # Importing getpass module

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    if score == 5:
        return "Strong"
    elif score == 4:
        return "Moderate"
    else:
        return "Weak"

# Use getpass to hide the password input
password = getpass.getpass("Enter a password to check its strength: ")

# Print the password strength result
print(f"Password strength: {check_password_strength(password)}")
