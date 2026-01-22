import hashlib
import os

FILE = "users.txt"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def signup():
    username = input("Username: ")
    password = input("Password: ")

    hashed = hash_password(password)

    with open(FILE, "a") as f:
        f.write(f"{username},{hashed}\n")

    print("Signup successful!")


def login():
    username = input("Username: ")
    password = input("Password")

    hashed = hash_password(password)

    if not os.path.exists(FILE):
        print("No users found!")
        return

    with open(FILE, "r") as f:
        for line in f:
            u, p = line.strip().split(",")

            if u == username and p == hashed:
                print("Login success!")
                return

    print("Invalid credentials!")


while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    ch = input("Choose: ")

    if ch == "1":
        signup()
    elif ch == "2":
        login()
    elif ch == "3":
        break
