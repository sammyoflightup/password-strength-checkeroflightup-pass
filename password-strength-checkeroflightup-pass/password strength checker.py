import re
def check_password_strength(password):
    length = len(password)
    if length < 10:
        return "Weak: Password is too short. It should be at least 10 characters long."

    # Check for various character types
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    if not has_upper:
        return "Weak: Password should contain at least one uppercase letter."
    if not has_lower:
        return "Weak: Password should contain at least one lowercase letter."
    if not has_digit:
        return "Weak: Password should contain at least one digit."
    if not has_special:
        return "Weak: Password should contain at least one special character."

    # Check for common patterns
    common_patterns = [r'123', r'password', r'abc', r'qwerty', r'password123']
    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            return "Weak: Password contains common patterns or sequences."

    return "Strong: Password meets all the strength criteria."

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()
