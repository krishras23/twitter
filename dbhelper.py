from mysql.connector import connect, Error

from hash import hashed


def write_to_db(twitter_query):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(twitter_query)
                connection.commit()
                return ""
    except Error as e:
        print(e)


def grabUserID(username, password):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            ID_list = []
            login_query = "select userID from twitter.users where username = \"{}\" and " \
                          "userPassword = \"{}\"".format(username, password)
            with connection.cursor() as cursor:
                cursor.execute(login_query)
                for record in cursor:
                    ID_list.append(record)
                return ID_list
    except Error as e:
        print(e)


def follow(follower, following):
    follow_query = "INSERT into twitter.followers (follower, following) values" \
                      " (\"{}\", \"{}\");".format(follower, following)
    write_to_db(follow_query)


def make_user(username, password, email):
    make_user_query = "INSERT INTO twitter.users (username, userPassword, email) values" \
                      " (\"{}\", \"{}\", \"{}\");".format(username, password, email)
    write_to_db(make_user_query)
    ID = grabUserID(username, password)
    print(ID)


def delete_user(username, password):
    delete_user_query = "DELETE from twitter.users where username = \"{}\" " \
                        "and userPassword = \"{}\"".format(username, password)
    write_to_db(delete_user_query)
    print(delete_user_query)


def make_tweet(username, tweet):
    tweet_query = "INSERT into twitter.tweet (username, message) values (\"{}\", \"{}\");".format(username, tweet)
    write_to_db(tweet_query)
    print(tweet_query)


def see_tweets():
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            tweets = []
            get_tweets_query = "select username, tweet from twitter.tweet"
            with connection.cursor() as cursor:
                cursor.execute(get_tweets_query)
                for record in cursor:
                    tweets.append(record)
                return tweets
    except Error as e:
        print(e)


def login(username, password):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            login_combination = []
            new_password = hashed(password)
            login_query = "select username, UserPassword from twitter.users where username = \"{}\" and " \
                          "userPassword = \"{}\"".format(username, new_password)
            with connection.cursor() as cursor:
                cursor.execute(login_query)
                for record in cursor:
                    login_combination.append(record)
                return login_combination
    except Error as e:
        print(e)


follow("krish", "some oen")