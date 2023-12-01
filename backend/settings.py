import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = 'fldkfslk893457sfd89fsd'

class Settings(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_CONNECT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False