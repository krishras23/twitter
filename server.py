import json
import flask
from flask_cors import CORS
from flask import request, Response, jsonify
from dbhelper import make_user, delete_user, login, make_tweet, see_tweets
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
    # if check_username(username) and check_password(password) == False:
    #     return Response("Username or password does not abide with the guidelines")
    HashedPassword = hashed(password)
    email = data["email"]
    make_user(username, HashedPassword, email)
    # return flask.redirect("127.0.0.1/login")
    return "Success"


@app.route('/login', methods=["POST"])
def logging_in():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    if len(login(username, password)) > 0:
        return Response("Success", status=200, mimetype='application/json')
    else:
        return Response("Username/Password Not Found")


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


@app.route('/tweet', methods=["POST"])
def tweeting():
    data = request.get_json()
    tweet = data["tweet"]
    username = data["username"]
    make_tweet(username, tweet)
    return ""


@app.route('/see_tweets', methods=["GET"])
def getting_tweets():
    tweets = see_tweets()
    return jsonify(tweets)


app.run()
