from .main import db, USERS


users = db(USERS)


def make_new_user(email: str, auth_token: str) -> dict:
    return {
        'email': email,
        'auth_token': auth_token,
    }


def save_user_to_db(user: dict) -> None:
    users.insert_one(user)


def get_user_by_auth_token(token):
    return users.find_one({'auth_token': token})


def get_user_by_email(email):
    return users.find_one({'email': email})
