from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "tictak"
def app_runner():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "asfafasf"



    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    from .ai import ai
    from .views import views
    from .auth import auth
    app.register_blueprint(ai, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_db(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'views.index'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    app.run(debug=True)



def create_db(app):
    if not path.exists(f'/webapp{DB_NAME}'):
        with app.app_context():
            db.create_all()
        print("DB Created Baby!")   
