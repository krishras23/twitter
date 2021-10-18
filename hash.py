import hashlib


def Hashed(password):
    hashed_value = hashlib.md5(password.encode())
    return hashed_value.hexdigest()


