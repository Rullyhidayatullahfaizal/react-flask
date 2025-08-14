from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)
    
    db.init_app(app)
    from app import models # noqa: F401 

    from .routes.task_routes import task_bp
    from app.routes.todo_routes import todo_bp
    # CORS(task_bp, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)
    app.register_blueprint(task_bp)
    app.register_blueprint(todo_bp)

    @app.get("/health")
    def health():
        return {"ok": True}

    return app
