import hashlib
import bcrypt
import re
import uuid

# 用來放一些工具函數
def generate_uuid(input_string: str):
    # 將輸入字串轉換為 UTF-8 編碼
    input_bytes = input_string.encode('utf-8')
    
    # 使用 SHA-256 加密演算法加密字串
    encrypted_uuid = hashlib.sha256(input_bytes).hexdigest()
    
    return encrypted_uuid[:20]

def generate_session_id():
    return str(uuid.uuid4())

def encrypt_password(password: str):
    hash_pwd = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hash_pwd.decode("utf-8")

def check_password(password: str, true_password: str):
    """
    password: str -> don't input hashed password, just original user input
    true_password: str -> hashed password in database
    """
    return bcrypt.checkpw(password.encode("utf-8"), true_password.encode("utf-8"))

def check_email(email: str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.fullmatch(regex, email) is not None