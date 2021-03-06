import json
import flask
from flask_cors import CORS
from flask import request, Response, jsonify
from dbhelper import make_user, delete_user, login, make_tweet, see_tweets, grabUserID
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
    userInfo = login(username, password)
    if len(userInfo) > 0:
        # this means success so grab the user id from database
        print('got username as ' + userInfo[0])
        print('set cookie for user')
        res = flask.make_response()
        res.delete_cookie('username')
        res.set_cookie('username2', userInfo[0])
        res.status = 200
        res.mimetype = 'application/json'
        return res
    else:
        return Response("Username or Password was not found")


@app.route('/delete_user', methods=["DELETE"])
def deleting_user():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    HashedPassword = hashed(password)
    delete_user(username, HashedPassword)
    return ""


# @app.route('/set_cookie', methods=["GET"])
# def set_cookie():
#     res = flask.make_response("Cookie is set")
#     res.set_cookie("username", value="Valid cookie")
#     return res
#

@app.route('/tweet', methods=["POST"])
def tweeting():
    data = request.get_json()
    tweet = data["tweet"]
    print(request)
    # cookieUserName = request.cookies.get('username2')
    # print("did we get any cookie -- " + cookieUserName)
    username = data["username"]
    make_tweet(username, tweet)
    return username


@app.route('/see_tweets', methods=["GET"])
def getting_tweets():
    tweets = see_tweets()
    return jsonify(tweets)


app.run()
