import binascii
import os

from .facebook_auth import get_user_email_from_facebook
from reporting.db.gateway import get_user_by_email, make_new_user, save_user_to_db


def generate_new_token():
    return binascii.hexlify(os.urandom(20)).decode()


def generate_auth_token_using_facebook_token(facebook_token):
    email = get_user_email_from_facebook(facebook_token)

    user = get_user_by_email(email)
    if not user:
        user = make_new_user(email, generate_new_token())
        save_user_to_db(user)

    return user['auth_token']
