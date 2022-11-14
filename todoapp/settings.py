# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    TODOAPP_LOCALES = ['en_US', 'zh_Hans_CN']
    todoapp_ITEM_PER_PAGE = 20

    BABEL_DEFAULT_LOCALE = TODOAPP_LOCALES[0]

    # SERVER_NAME = 'todoapp.dev:5000'  # enable subdomain support
    SECRET_KEY = os.getenv('SECRET_KEY', 'a secret string')

    SQLALCHEMY_DATABASE_URI = "postgres://databaseadmin:neUZxjeVzA1kGxVHBTYP9xunqX6WZ1Qx@dpg-cdp4c69a6gdooi1cidd0-a.oregon-postgres.render.com/shareddatabase"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
