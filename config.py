import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'asdfgfhhfhgfgjjfdfddvgbbfgnf'  # should be moved to environment variables in production


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://slwukubt:WcTJ9PLNSTBu9_s0wTFCCbwE3BFdd6J8@stampy.db.elephantsql.com:5432/slwukubt'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://slwukubt:WcTJ9PLNSTBu9_s0wTFCCbwE3BFdd6J8@stampy.db.elephantsql.com:5432/slwukubt'
