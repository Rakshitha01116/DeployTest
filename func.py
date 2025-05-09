import re

def is_valid_email(email):
    """Check if the email is in a valid format: username@domain.com"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.match(pattern, email))

# Example usage
print(is_valid_email("user@domain.com"))   # Output: True
print(is_valid_email("user@domain"))       # Output: False
