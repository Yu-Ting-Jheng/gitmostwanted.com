class Config(object):
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_ECHO = False
    SECRET_KEY = ''
    TESTING = False
    DEBUG = True


class ConfigDevelopment(Config):
    SQLALCHEMY_ECHO = True
    TESTING = True


class ConfigProduction(Config):
    DEBUG = False
