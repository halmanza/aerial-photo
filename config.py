class Config(object):
    debug = False
    Testing = False
    SECRET_KEY = b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G'

    MAIL_NAME_INBOX = 'dev.coffeeforlife@gmail.com'
    MAIL_ACCOUNT = 'dev.coffeeforlife@gmail.com'
    MAIL_PASSWORD = 'Mesa1989!'

    SESSION_COOK_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    Debug = True

    SESSION_COOK_SECURE = False


class TestingConfig(Config):
    TESTING = True
