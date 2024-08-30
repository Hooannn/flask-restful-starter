from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase
import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = settings.BUNDLE_ERRORS

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
api = Api(app)
api.prefix = '/api/v1'
migrate = Migrate(app, db)

from modules.users.model import User
from modules.users.resource import UsersResource, UserResource

api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<user_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)