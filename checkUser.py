special_char = ["!", "@", "#", "$", "%", "^", "&", "*", "()", "-",
                "+", "?", "_", "=", ",", "<", ">", "/"]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def check_username(username):
    if len(username) < 7 or len(username) > 30:
        return False  # Username is not correct length
    else:
        return username


def check_password(password):
    if len(password) < 7 or len(password) > 30:
        return False  # Password is not correct length
    for x in password:
        for y in special_char:
            if x == y:
                return password  # Welcome to twitter!
    return False  # Password requires a special character


def user(username, password):
    if username == False or password == False:
        return "Username or password does not abide to guidelines"
    else:
        return "Welcome to twitter" + username
