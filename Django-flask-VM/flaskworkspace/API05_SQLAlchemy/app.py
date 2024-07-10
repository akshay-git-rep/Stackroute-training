from flask_smorest import Api
from flask import Flask, request, jsonify
from resources.store import store_blp
from resources.item import item_blp
from flask_migrate import Migrate
import os
from db import db
# from resources.item import item_blp
# from resources.store import store_blp


app = Flask(__name__)

app.config["API_TITLE"] = "Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        # "DATABASE_URL", "sqlite:///data.db")

    # create mysql database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        'DATABASE_URL', 'mysql+pymysql://root:root1234@localhost:3306/stores_db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

api = Api(app)

migrate = Migrate(app, db)

# Create all tables in the database before starting the server
# with app.app_context():
#     db.create_all()

api.register_blueprint(item_blp)
api.register_blueprint(store_blp)