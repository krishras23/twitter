special_char = ["!", "@", "#", "$", "%", "^", "&", "*", "()", "-",
                "+", "?", "_", "=", ",", "<", ">", "/", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def check_username(username):
    if len(username) < 5 or len(username) > 30:
        return False
    else:
        return True


def check_password(password):
    if len(password) < 7 or len(password) > 30:
        return False
    for x in password:
        for y in special_char:
            if x == y:
                return True
    return False


def check_email(email):
    char = "@"
    if char in email:
        return True
    return False
