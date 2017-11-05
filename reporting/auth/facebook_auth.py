import json
import os

from rauth import OAuth2Service


FACEBOOK_ID = os.environ.get('FACEBOOK_ID')
FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')


def get_user_email_from_facebook(facebook_token):
    oauth = FacebookAuth(facebook_token)
    social_id, email = oauth.get_user_data()

    if social_id is None:
        return None

    return email


class FacebookAuth:

    def __init__(self, facebook_token):
        self.fb_token = facebook_token
        self.consumer_id = FACEBOOK_ID
        self.consumer_secret = FACEBOOK_SECRET
        self.service = OAuth2Service(
            name='facebook',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://graph.facebook.com/oauth/authorize',
            access_token_url='https://graph.facebook.com/oauth/access_token',
            base_url='https://graph.facebook.com/'
        )

    def get_user_data(self):
        def decode_json(payload):
            return json.loads(payload.decode('utf-8'))

        oauth_session = self.service.get_auth_session(
            data={'code': self.fb_token,
                  'grant_type': 'authorization_code',
                  'redirect_uri': 'https://www.facebook.com/connect/login_success.html'},
            decoder=decode_json,
        )
        me = oauth_session.get('me').json()
        return (
            'facebook$' + me['id'],
            me.get('email')
        )
