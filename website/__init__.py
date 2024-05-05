from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__file__))



db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dASVNJFOIDSL/VDNDSS'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'website', DB_NAME)
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    from .models import User, Note
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view= 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    db_path = os.path.join(basedir, 'website')
    if not os.path.exists(db_path):
        os.makedirs(db_path)
    if not os.path.exists(os.path.join(db_path, DB_NAME)):
        with app.app_context():
            db.create_all()
            print('Created Database!')
