class Config:
    # Basic configuration
    DEBUG = True
    TESTING = True

    #Database configuration

class ProductionConfig:
    DEBUG = False

class DevelopmentConfig:
    DEBUG = True
    TESTING = True