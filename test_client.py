import requests


def checkStatus(payload):
    x = requests.post(url="http://127.0.0.1:5000/create_user", json=payload)
    if x.status_code == 200:
        print('Success!')
    elif x.status_code == 500 or x.status_code == 501:
        print("Not Found. Please try again.")


# no username key
checkStatus({"": "hulk", "password": "password", "email": "jsonify.com"})

# no password key
checkStatus({"username": "iamgroot", "": "password", "email": "jsonify.com"})
# no email key
checkStatus({"username": "sneaky32", "password": "password", "": "jsonify.com"})

checkStatus({"username": "ninja56", "password": "password", "email": "jsonify.com"})

