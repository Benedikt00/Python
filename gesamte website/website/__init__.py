from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2B1A58D8AA41297E24D8ADAA8A548'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app


