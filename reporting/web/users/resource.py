import json

import falcon

from reporting.auth.token_auth import generate_auth_token_using_facebook_token


class UserResource:

    auth = {
        'exempt_methods': ['POST']
    }

    def on_get(self, req, resp):
        resp.body = 'This resource requires authentication'

    def on_post(self, req, resp):
        resp.body = "This resource uses token authentication"


class FacebookResource:

    auth = {
        'exempt_methods': ['POST']
    }

    def on_post(self, req, resp):
        auth_token = generate_auth_token_using_facebook_token(req.get_param('facebook_token'))
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'auth_token': auth_token})
