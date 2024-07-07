import secrets
import string
import webbrowser
import urllib.parse

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4")
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password_characters = [
        secrets.choice(lowercase_letters),
        secrets.choice(uppercase_letters),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password_characters += [secrets.choice(all_characters) for _ in range(length - 4)]
    
    secrets.SystemRandom().shuffle(password_characters)
    
    return ''.join(password_characters)

def share_on_linkedin(email, password):
    message = f"I've just generated a secure password for {email}: {password}"
    encoded_message = urllib.parse.quote(message)
    linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_message}"
    webbrowser.open(linkedin_url)

def main():
    email = input("Enter your email address: ")
    password_length = int(input("Enter desired password length (minimum 4): "))
    password = generate_password(password_length)
    print(f"Generated password for {email}: {password}")
    
    share = input("Would you like to share this on LinkedIn? (yes/no): ").strip().lower()
    if share == 'yes':
        share_on_linkedin(email, password)
        print("Sharing on LinkedIn...")
    else:
        print("Password generation complete. Not shared on LinkedIn.")

if __name__ == "__main__":
    main()
