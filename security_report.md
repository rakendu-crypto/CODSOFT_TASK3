# Secure Code Assessment Report

## 1. Project Overview

This project demonstrates a security assessment of a Python-based user authentication application.

The assessment focuses on identifying common security vulnerabilities in the initial implementation and applying secure coding practices to improve the application.

## 2. Vulnerabilities Identified

### Vulnerability 1: Hardcoded Credentials

**Location:** `vulnerable_app.py`

The application contains username and password values directly inside the source code.

**Risk:**
- Credentials can be exposed if the source code is shared.
- Attackers may gain unauthorized access.

**Recommendation:**
Avoid storing credentials directly in source code. Use secure configuration or environment variables.

---

### Vulnerability 2: SQL Injection

**Location:** `vulnerable_app.py`

User input is directly concatenated into the SQL query.

**Risk:**
- Malicious input may modify the intended SQL query.
- This can lead to unauthorized database access or authentication bypass.

**Recommendation:**
Use parameterized SQL queries with placeholders.

**Secure implementation:**

```python
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))