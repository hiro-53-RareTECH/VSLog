# Flask設定ファイル
import os

class Config:
    # 共通設定
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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

class TestConfig(Config):
    TESTING = True
    # テスト用DB名
    MYSQL_DATABASE = os.getenv('MYSQL_TEST_DATABASE', 'app_test')
    SQLALCHEMY_DATABASE_URI = (
    f'mysql+pymysql://{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}'
    f'@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{MYSQL_DATABASE}'
    )

class UnitTestingConfig(Config):
    TESTING = True
    # 単体テストはSOLiteを使用して高速化
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
