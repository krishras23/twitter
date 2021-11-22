from mysql.connector import connect, Error


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


def make_user(username, password, email):
    make_user_query = "INSERT INTO twitter.users (username, userPassword, email) values" \
                      " (\"{}\", \"{}\", \"{}\");".format(username, password, email)
    write_to_db(make_user_query)
    print(make_user_query)


def delete_user(username, password):
    delete_user_query = "DELETE from twitter.users where username = \"{}\" " \
                        "and userPassword = \"{}\"".format(username, password)
    write_to_db(delete_user_query)
    print(delete_user_query)


def get_user_info():
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            userList = []
            get_user_info_query = "select username from twitter.users"
            with connection.cursor() as cursor:
                cursor.execute(get_user_info_query)
                for record in cursor:
                    userList.append(record)
                return userList
    except Error as e:
        print(e)


def check_user_info():
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            username_password = []
            getUsernamePassword_query = "select username, UserPassword from twitter.users"
            with connection.cursor() as cursor:
                cursor.execute(getUsernamePassword_query)
                for record in cursor:
                    username_password.append(record)
                return username_password
    except Error as e:
        print(e)


