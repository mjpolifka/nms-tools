from flask import Flask
# from satisfactory_tools.db import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # app.config.from_mapping(SQLALCHEMY_DATABASE_URI=f'sqlite:///database.db',
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False)
    
    # db.init_app(app)
    
    from nms_server import home
    app.register_blueprint(home.bp)
    
    return app