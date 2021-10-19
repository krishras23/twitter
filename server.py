import flask
from flask_cors import CORS
from flask import request, Response
from dbhelper import make_user, delete_user
from hash import Hashed

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/create_user', methods=["POST"])
def creating_user():
    data = request.get_json()
    username = data["username"]

    if "password" not in data:
        return Response("{'password':'not found'}", status=501, mimetype='application/json')
    password = data["password"]
    HashedPassword = Hashed(password)
    email = data["email"]
    make_user(username, HashedPassword, email)
    return ""


@app.route('/delete_user', methods=["DELETE"])
def deleting_user():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    HashedPassword = Hashed(password)
    delete_user(username, HashedPassword)
    return ""


app.run()
