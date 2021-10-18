import flask
from flask_cors import CORS
from flask import request, jsonify
from dbhelper import make_user, delete_user
from hash import Hashed

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/create_user', methods=["POST"])
def creating_user():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    HashedPassword = Hashed(password)
    email = data["email"]
    make_user(username, HashedPassword, email)
    resp = jsonify(success=True)
    # find a better way to show status codes
    return resp


@app.route('/delete_user', methods=["DELETE"])
def deleting_user():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    HashedPassword = Hashed(password)
    delete_user(username, HashedPassword)
    return ""


app.run()
