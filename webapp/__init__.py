from flask import Flask
def app_runner():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "asfafasf"
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.run(debug=True)
