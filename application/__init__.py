import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

from config import config_by_name

db = SQLAlchemy()

from application import db
from application.models import User

def create_app():
    from flask_potion import Api

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(
        config_by_name[os.environ.get('FLASK_ENV', 'dev')])

    app.logger.info('Connecting database')
    db.init_app(app)

    app.logger.info('Setting JWT Authenticator')
    jwt = JWTManager(app)


    @app.route('/login', methods=['POST'])
    def login():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        if username != 'test' or password != 'test':
            return jsonify({"msg": "Bad username or password"}), 401

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    @app.route('/', methods=['GET'])
    def index():
        return 'Qual foi?'

    app.logger.info('creating Flask-Potion Apis')
    from application import apis
    api = Api(app, prefix='/api/v1', title='Backend API')
    apis.create_api(api)

    app.logger.info('Finished initialization')

    return app
