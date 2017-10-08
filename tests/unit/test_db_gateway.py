import pytest

from reporting.db.gateway import (
    get_user_by_auth_token,
    get_user_by_email,
    make_new_user,
    save_user_to_db,
)
from reporting.db.main import db, USERS


def test_user_object_has_correct_fields():
    user = make_new_user(email='test@test.com')
    assert 'email' in user
    assert 'auth_token' in user


def test_new_user_is_saved_to_db():
    new_user = make_new_user('test@test.com')
    save_user_to_db(new_user)

    assert db(USERS).find_one({'email': 'test@test.com'}) is not None


def test_existing_user_is_not_duplicated_in_db_and_token_is_returned():
    assert 0


def test_user_found_for_good_token(test_user):
    assert get_user_by_auth_token(test_user['auth_token']) is not None


def test_user_not_found_for_bad_token():
    assert get_user_by_auth_token('bad_token') is None
    assert get_user_by_auth_token('') is None


class TestUserSearchByEmail:

    def test_existing_user_is_found(self, test_user):
        assert get_user_by_email(test_user['email'])['email'] == test_user['email']

    def test_nonexisting_user_returns_none(self):
        assert get_user_by_email('bad_email@email.com') is None
