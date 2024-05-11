import hashlib
import bcrypt

# 用來放一些工具函數

def generate_uuid(input_string: str):
    # 將輸入字串轉換為 UTF-8 編碼
    input_bytes = input_string.encode('utf-8')
    
    # 使用 SHA-256 加密演算法加密字串
    encrypted_uuid = hashlib.sha256(input_bytes).hexdigest()
    
    return encrypted_uuid[:20]

def encrypt_password(password: str):
    hash_pwd = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hash_pwd.decode("utf-8")