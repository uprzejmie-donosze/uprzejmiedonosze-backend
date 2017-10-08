import binascii
import os


def generate_new_token():
    return binascii.hexlify(os.urandom(20)).decode()
