from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "webapptest1.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dslkjdf sdfjjf'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://webapptest1_user:rHSUGf2nExjIq7c5xJv6et8sfbdDhk3t@dpg-ch4kj964dad97s4a83ig-a/webapptest1'
    db.init_app(app) 

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

#def create_database(app):
 #   if not path.exists('website/' + DB_NAME):
  #      db.create_all(app=app)
   #     print('Created Database!')
