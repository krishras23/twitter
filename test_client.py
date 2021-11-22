import requests


def check_status(payload):
    x = requests.post(url="http://127.0.0.1:5000/create_user", json=payload)
    if x.status_code == 200:
        print('Success!')
    elif x.status_code == 500 or x.status_code == 501:
        print("Not Found. Please try again.")


# no username key
check_status({"": "hulk", "password": "password", "email": "jsonify.com"})
# no password key
check_status({"username": "iamgroot", "": "password", "email": "jsonify.com"})
# no email key
check_status({"username": "sneaky32", "password": "password", "": "jsonify.com"})
check_status({"username": "ninja56", "password": "password", "email": "jsonify.com"})
