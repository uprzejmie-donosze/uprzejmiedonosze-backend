import pytest
from webtest.app import AppError

from reporting.web.http_statuses import HTTPStatusCodes
from tests.testutils import TestApp


test_app = TestApp()


class TestAPITokenAuthentication():

    def test_endpoints_require_token_authentication(self):
        with pytest.raises(AppError) as err:
            test_app.app.get('http://localhost:8000/user', headers=test_app.headers)
            assert HTTPStatusCodes.UNAUTHORIZED_ACCESS_401 in err.value

    def test_user_POST_doesnt_require_token_authentication(self):
        response = test_app.app.post('http://localhost:8000/user')
        assert response.status_code == HTTPStatusCodes.OKAY_200

    def test_api_call_with_bad_token_leads_to_unauthorized_access_response(self):
        test_app.headers['Authorization'] = 'Token badtoken'
        with pytest.raises(AppError) as err:
            test_app.app.get('http://localhost:8000/user', headers=test_app.headers)
            assert HTTPStatusCodes.UNAUTHORIZED_ACCESS_401 in err.value

    def test_api_call_with_good_token_goes_through(self, test_user):
        test_app.headers['Authorization'] = f'Token {test_user["auth_token"]}'
        response = test_app.app.post('http://localhost:8000/user')
        assert response.status_code == HTTPStatusCodes.OKAY_200
