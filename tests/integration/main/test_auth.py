from unittest import mock

import pytest
from webtest.app import AppError

from reporting.auth.token_auth import generate_auth_token_using_facebook_token
from reporting.db.main import db, USERS
from reporting.web.http_statuses import HTTPStatusCodes
from tests.testutils import TestApp


test_app = TestApp()


class TestAPITokenAuthentication():

    def test_user_endpoint_requires_token_authentication(self):
        with pytest.raises(AppError) as err:
            test_app.app.get('http://localhost:8000/user', headers=test_app.headers)
            assert HTTPStatusCodes.UNAUTHORIZED_ACCESS_401 in err.value

    def test_user_resource_POST_doesnt_require_token_authentication(self):
        response = test_app.app.post('http://localhost:8000/user')
        assert response.status_code == HTTPStatusCodes.OKAY_200

    def test_user_resource_api_call_with_bad_token_leads_to_unauthorized_access_response(self):
        test_app.headers['Authorization'] = 'Token badtoken'
        with pytest.raises(AppError) as err:
            test_app.app.get('http://localhost:8000/user', headers=test_app.headers)
            assert HTTPStatusCodes.UNAUTHORIZED_ACCESS_401 in err.value

    def test_user_resource_api_call_with_good_token_goes_through(self, test_user):
        test_app.headers['Authorization'] = f'Token {test_user["auth_token"]}'
        response = test_app.app.get('http://localhost:8000/user', headers=test_app.headers)
        assert response.status_code == HTTPStatusCodes.OKAY_200

    @mock.patch('reporting.web.users.resource.generate_auth_token_using_facebook_token')
    def test_facebook_resource_endpoint_doesnt_require_token_for_POST(self, mocked_func):
        mocked_func.return_value = 'test_auth_token'
        response = test_app.app.post('http://localhost:8000/user/facebook?facebook_token=fake_fb_token')
        assert response.status_code == HTTPStatusCodes.OKAY_200


class TestGenerateAuthTokenUsingFacebookToken:

    @mock.patch('reporting.auth.token_auth.get_user_email_from_facebook')
    def test_no_duplicate_user_is_made_when_user_already_exists(self, mocked_func, test_user):
        assert db(USERS).find({'email': test_user['email']}).count() == 1

        mocked_func.return_value = test_user['email']

        generate_auth_token_using_facebook_token('fake_fb_token')

        assert db(USERS).find({'email': test_user['email']}).count() == 1

    @mock.patch('reporting.auth.token_auth.get_user_email_from_facebook')
    def test_duplicate_user_doesnt_get_new_auth_token(self, mocked_func, test_user):
        prev_token = db(USERS).find_one({'email': test_user['email']})['auth_token']
        mocked_func.return_value = test_user['email']

        generate_auth_token_using_facebook_token('fake_fb_token')

        assert db(USERS).find_one({'email': test_user['email']})['auth_token'] == prev_token

    @mock.patch('reporting.auth.token_auth.get_user_email_from_facebook')
    def test_new_user_is_persisted_in_db(self, mocked_func):
        test_email = 'test@test.com'
        mocked_func.return_value = test_email
        
        assert db(USERS).find({'email': test_email}).count() == 0

        generate_auth_token_using_facebook_token('fake_fb_token')

        assert db(USERS).find({'email': test_email}).count() == 1
        assert db(USERS).find_one({'email': test_email})['auth_token'] is not None
