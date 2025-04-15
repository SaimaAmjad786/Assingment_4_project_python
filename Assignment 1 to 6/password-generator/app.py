# Project 6 : Password Generator in Python

import random
import string

try:
    import pyperclip
    clipboard_available = True
except ImportError:
    clipboard_available = False

def generate_password(length=12):
    """Generates a strong random password with required character types."""
    if length < 4:
        return None, "❌ Password length must be at least 4 characters."

    # Character pools
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    # Combine all character types
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = random.choices(all_chars, k=length - 4)

    # Create and shuffle password
    password_list = [lower, upper, digit, symbol] + remaining
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password, None

def evaluate_strength(length):
    """Returns a basic assessment of password strength based on length."""
    if length < 6:
        return "🔴 Weak"
    elif length < 10:
        return "🟡 Medium"
    else:
        return "🟢 Strong"

def main():
    print("🔐 Welcome to the Professional Password Generator\n")
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        password, error = generate_password(length)

        if error:
            print(error)
            return

        print("\n✅ Your Generated Password:", password)
        print("🔎 Password Strength:", evaluate_strength(length))

        if clipboard_available:
            pyperclip.copy(password)
            print("📋 Password copied to clipboard!")
        else:
            print("📎 Tip: Install 'pyperclip' to enable auto-copy to clipboard.")

    except ValueError:
        print("⚠️  Please enter a valid number.")

if __name__ == "__main__":
    main()
