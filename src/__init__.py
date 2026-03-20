# アプリファクトリ
from dotenv import load_dotenv
from flask import Flask, render_template

from .config import Config
from .extensions import db, migrate, login_manager

def create_app(config_object=Config, *, load_env: bool = True) -> Flask:
    # .envファイルの読み込み（カレントディレクトリがルートである前提）
    if load_env:
        load_dotenv()
    
    app = Flask(__name__)
    app.config.from_object(config_object)

    # extensionsを初期化
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # 未認証のユーザーがリダイレクトされるビュー関数とメッセージを設定
    login_manager.login_view = 'auth.login_view'
    login_manager.login_message = 'ログインが必要です。先にログインしてください。'

    @login_manager.user_loader
    def load_user(user_id):
        from .models.users import User
        return User.query.get(user_id)
    
    # models読み込み
    from . import models

    # Blueprint登録
    from .blueprints.auth import auth_bp
    from .blueprints.profile import profile_bp
    from .blueprints.study import study_bp
    from .blueprints.error import error_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(study_bp)
    app.register_blueprint(error_bp)

    # 404エラー時の処理
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html'), 404

    return app
