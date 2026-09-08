# CODSOFT_TASK3
cybersecurity internship task 3

# CODSOFT Task 3 – Secure Code Assessment

## Project Overview

This project focuses on identifying security vulnerabilities in a Python-based user authentication application and applying secure coding practices to improve its security.

## Objectives

- Identify common security vulnerabilities.
- Analyze insecure coding practices.
- Implement secure coding techniques.
- Test the improved authentication system.

## Files

- `vulnerable_app.py` – Initial application containing security weaknesses.
- `secure_app.py` – Improved version with security fixes.
- `setup_database.py` – Creates and initializes the secure database.
- `security_report.md` – Detailed vulnerability assessment and fixes.
- `users.db` – Local SQLite database created during testing.

## Vulnerabilities Identified

### 1. Hardcoded Credentials
Credentials were directly stored in the source code.

### 2. SQL Injection
User input was directly concatenated into an SQL query.

### 3. Plain-Text Password Handling
The initial implementation did not securely protect passwords.

## Security Improvements

- Parameterized SQL queries
- Password hashing using PBKDF2
- Random salt generation
- Improved authentication handling
- Secure database initialization

## Testing

### Valid Login

Username:
`admin`

Password:
`admin123`

Result:

`Login successful!`

### Invalid Login

An incorrect password was tested.

Result:

`Invalid username or password.`

## Conclusion

The project demonstrates how security vulnerabilities can be identified through code assessment and mitigated using secure coding practices.

This assessment highlights the importance of secure authentication, proper input handling, and password protection in application development.