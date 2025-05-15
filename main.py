import json
from cryptography.fernet import Fernet


# Key generation and loading functions
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


# Encryption/decryption functions
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()  # Fixed this line


# Password management functions
def add_password(service, username, password):
    data = {}
    try:
        with open("passwords.json", "r") as f:  # Fixed filename consistency
            data = json.load(f)
    except FileNotFoundError:
        pass

    data[service] = {
        "username": username,
        "password": encrypt_password(password)
    }

    with open("passwords.json", "w") as f:
        json.dump(data, f, indent=4)


def get_password(service):
    try:
        with open("passwords.json", "r") as f:  # Fixed filename consistency
            data = json.load(f)
            if service in data:
                decrypted = decrypt_password(data[service]["password"])
                return f"Username: {data[service]['username']}\nPassword: {decrypted}"
            return "Service not found!"
    except FileNotFoundError:
        return "No passwords stored yet."


def main():
    try:
        load_key()
    except FileNotFoundError:
        generate_key()

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            service = input("Service (e.g., Google, Instagram): ")
            username = input("Username: ")
            password = input("Password: ")
            add_password(service, username, password)
            print("Password saved!")

        elif choice == "2":
            service = input("Service to retrieve: ")
            print(get_password(service))

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()