class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345678@localhost/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'something_very_secret'

    ### Flask security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'