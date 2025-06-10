from cryptography.fernet import Fernet
import bcrypt
import base64
import os

FERNET_KEY = os.environ.get("FERNET_KEY") or Fernet.generate_key()
fernet = Fernet(FERNET_KEY)

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def encrypt_email(email: str) -> str:
    return fernet.encrypt(email.encode()).decode()

def decrypt_email(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
