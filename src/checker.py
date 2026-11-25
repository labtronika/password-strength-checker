"""
Password evaluation engine

"""
from sympy import evaluate


MIN_PASSWORD_LENGTH = 12

COMMON_PASSWORDS = {
    "password123",
    "password321"
    "123password",
    "123456789",
    "qwertyuiop",
    "admin1234",
    "admin12345",
    "123admin",
    "adminkita",
    "kitaadmin",
}

def check_length(password: str) -> bool:
    return len(password) >= MIN_PASSWORD_LENGTH

def check_common_passwords(password: str) -> bool:
    return password in COMMON_PASSWORDS

def check_lowercase(password: str) -> bool:
    return any(char.islower() for char in password)

def check_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)

