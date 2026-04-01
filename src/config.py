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
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = "5432"
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    )

class UnitTestingConfig(Config):
    TESTING = True

    # テスト用設定
    SERVER_NAME = 'localhost'
    PROPAGATE_EXCEPTIONS = False

    # テスト用MySQL設定
    is_postgres = os.getenv("IS_POSTGRES", "false").lower() == "true"

    # テスト用PostgreSQL設定
    if is_postgres:
        POSTGRES_TEST_USER = os.getenv("POSTGRES_TEST_USER")
        POSTGRES_TEST_PASSWORD = os.getenv("POSTGRES_TEST_PASSWORD")
        POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
        POSTGRES_PORT = "5432"
        POSTGRES_TEST_DATABASE = os.getenv("POSTGRES_TEST_DATABASE")

        SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{POSTGRES_TEST_USER}:{POSTGRES_TEST_PASSWORD}'
        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_TEST_DATABASE}'
    )
    
    else:
        MYSQL_USER = os.getenv("MYSQL_TEST_USER")
        MYSQL_PASSWORD = os.getenv("MYSQL_TEST_PASSWORD")
        MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
        MYSQL_PORT = "3306"
        MYSQL_DATABASE = os.getenv("MYSQL_TEST_DATABASE")

        SQLALCHEMY_DATABASE_URI = (
        f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}'
        f'@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
        )
