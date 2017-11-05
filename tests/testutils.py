import pytest
import webtest

from reporting.db.gateway import (
    get_user_by_email,
    make_new_user,
    save_user_to_db,
)
from reporting.db.main import db, USERS
from reporting.main import main


container = main()


class TestApp:

    def __init__(self):
        self.app = webtest.TestApp(container('web.wsgi.app'))
        self.headers = {'Content-Type': 'application/json'}
        self.headers['Authorization'] = 'Token testing'


@pytest.fixture()
def test_user():
    test_user =  make_new_user('test@test.com', 'test_token')
    save_user_to_db(test_user)
    yield test_user
    db(USERS).delete_many({})

