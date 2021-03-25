import os

# set the base directory
basedir = os.path.abspath(os.path.dirname(__name__))


# Create the super class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


# Create the development config
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'dev-data.db')


# Create the testing config
class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test-data.db')


# create the production config
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
