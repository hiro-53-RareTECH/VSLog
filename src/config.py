# Flask設定ファイル
import os

class Config:
    # 共通設定
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    # MySQL設定
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = "3306"
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    SQLALCHEMY_DATABASE_URI = (
        f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}'
        f'@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
    )

class ProductionConfig(Config):
    # 本番用Flask設定
    SESSION_COOKIE_SECURE = True
    SERVER_NAME = "https://vslog.onrender.com"

    # PostgreSQL設定
    DATABASE_URL = os.getenv("DATABASE_URL")
    POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
    POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
    POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
    POSTGRESQL_PORT = "5432"
    POSTGRESQL_DATABASE = os.getenv("POSTGRESQL_DATABASE")

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}'
        f'@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}'
    )

class UnitTestingConfig(Config):
    TESTING = True

    # テスト用設定
    SERVER_NAME = 'localhost'
    PROPAGATE_EXCEPTIONS = False

    # テスト用MySQL設定
    MYSQL_USER = os.getenv("MYSQL_TEST_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_TEST_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = "3306"
    MYSQL_DATABASE = os.getenv("MYSQL_TEST_DATABASE")

    SQLALCHEMY_DATABASE_URI = (
    f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}'
    f'@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
    )

