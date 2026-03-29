# gunicorn "wsgi:app" の入口
from src import create_app
from src.config import ProductionConfig

app = create_app()

if __name__ == '__main__':
    app.run()
