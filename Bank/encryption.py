import hashlib
def encrypt(s):
    return hashlib.sha512(str(s).encode()).hexdigest()