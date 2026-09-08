import sqlite3
import hashlib
import os

def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT password_hash, salt FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    user = cursor.fetchone()
    conn.close()

    if user:
        stored_hash, salt = user
        password_hash = hash_password(password, salt)

        if password_hash == stored_hash:
            print("Login successful!")
            return

    print("Invalid username or password.")

username = input("Enter username: ")
password = input("Enter password: ")

login(username, password)