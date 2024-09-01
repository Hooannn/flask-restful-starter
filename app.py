from flask import Flask, jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
from flask_migrate import Migrate
from routes import register_resources
from extensions import db, jwt, bcrypt
import settings

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = settings.JWT_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = settings.JWT_ACCESS_TOKEN_EXPIRES
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = settings.JWT_REFRESH_TOKEN_EXPIRES
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["BUNDLE_ERRORS"] = settings.BUNDLE_ERRORS


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

# Init extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)
################################

api = Api(app)
api.prefix = "/api/v1"
register_resources(api)
migrate = Migrate(app, db)

from models import *

if __name__ == "__main__":
    app.run(debug=True, port=5000)
