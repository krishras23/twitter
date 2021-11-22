import hashlib


def hashed(password):
    hashed_value = hashlib.md5(password.encode())
    return hashed_value.hexdigest()


