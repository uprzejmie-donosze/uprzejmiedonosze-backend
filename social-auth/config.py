SOCIAL_AUTH_FACEBOOK_LOGIN_URL = ''
SOCIAL_AUTH_TWITTER_KEY = 'foobar'
SOCIAL_AUTH_TWITTER_SECRET = 'bazqux'
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.FacebookOAuth',
)


# Used to redirect the user once the auth process ended successfully. The value of ?next=/foo is used if it was present
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'

# Some providers return a username, others just an ID or email or first and last names.
# The application tries to build a meaningful username when possible but defaults to generating one if needed.
# If you want to use the full email address as the username, define this setting.
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

