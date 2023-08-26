import os


class Config:
    ALGORITHM = "HS256"
    DEBUG = False


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    SECRET_KEY = "very-secret-key"
    DEBUG = True


config_by_name = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}