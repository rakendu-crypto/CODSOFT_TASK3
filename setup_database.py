import sqlite3
import hashlib
import os

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password_hash BLOB NOT NULL,
    salt BLOB NOT NULL
)
""")

username = "admin"
password = "admin123"

salt = os.urandom(16)

password_hash = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode(),
    salt,
    100000
)

cursor.execute(
    "INSERT OR REPLACE INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
    (username, password_hash, salt)
)

conn.commit()
conn.close()

print("Database setup completed successfully!")