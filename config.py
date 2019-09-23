import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://audrey:12345@localhost/personalblog'
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    
    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # Email Configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 4056
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('audreywncode.gmail.com')
    MAIL_PASSWORD = os.environ.get('C0de2019$')
    SENDER_EMAIL = 'audreywncode@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://audrey:12345@localhost/personalblog_test'
    DEBUG = True
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://audrey:12345@localhost/personalblog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}