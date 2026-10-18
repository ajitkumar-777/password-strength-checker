
import getpass
import string


def check_password_strength(password):
    """Return a strength rating and suggestions for a password."""
    if not password.strip():
        return "Invalid", ["Password cannot be empty."]
    
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions


def main():
    password = getpass.getpass("Enter a password: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nPassword strength: {strength}")

    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Your password meets all the basic checks.")


if __name__ == "__main__":
    main()
