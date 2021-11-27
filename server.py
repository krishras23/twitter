import flask
from flask_cors import CORS
from flask import request, Response, jsonify
from dbhelper import make_user, delete_user, get_user_info
from hash import hashed
from checkUser import check_username, check_password, check_email

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/create_user', methods=["POST"])
def creating_user():
    data = request.get_json()
    print(data)
    username = data["username"]
    password = data["password"]
    if check_username(username) and check_password(password) == False:
        return Response("{'Username or password':'does not abide with the guidelines'}")
    HashedPassword = hashed(password)
    email = data["email"]
    make_user(username, HashedPassword, email)
    # return flask.redirect("127.0.0.1/login")
    return "Success"


@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    if "password" not in data:
        return Response("{'password':'not found'}", status=501, mimetype='application/json')


@app.route('/delete_user', methods=["DELETE"])
def deleting_user():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    HashedPassword = hashed(password)
    delete_user(username, HashedPassword)
    return ""


@app.route('/set_cookie', methods=["GET"])
def set_cookie():
    res = flask.make_response("Cookie is set")
    res.set_cookie("username", value="Valid cookie")
    return res


app.run()
