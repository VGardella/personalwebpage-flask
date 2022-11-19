class Config:
    # Basic configuration
    DEBUG = True
    TESTING = True

    #Database configuration

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True