import os
import sys

from app import app

WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"

dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", dev_db)


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class HerokuConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)


config = {
    "development": DevelopmentConfig,
    "production":ProductionConfig,
    "heroku":HerokuConfig
}

