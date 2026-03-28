# アプリファクトリ
from flask import Flask, render_template

from .config import DevelopmentConfig
from .extensions import db, migrate, login_manager

def create_app(config_object=DevelopmentConfig) -> Flask:
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

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(study_bp)

    # エラー時の処理
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html'), 404
    
    @app.errorhandler(403)
    def forbidden_error(e):
        return render_template('error/403.html'), 403

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error/500.html'), 500

    return app
