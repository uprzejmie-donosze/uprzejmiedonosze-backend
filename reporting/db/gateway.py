from .main import db, USERS
from reporting.auth import generate_new_token


users = db(USERS)


def make_new_user(email: str) -> dict:
    return {
        'email': email,
        'auth_token': generate_new_token(),
    }


def save_user_to_db(user: dict) -> None:
    users.insert_one(user)


# def generate_new_auth_token_for_user(user):
#     users.update_one({'email': email}, {'$set': {'auth_token': generate_new_token()}})


def get_user_by_auth_token(token):
    return users.find_one({'auth_token': token})


def get_user_by_email(email):
    return users.find_one({'email': email})
