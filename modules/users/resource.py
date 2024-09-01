from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, fields, marshal, reqparse
from utils import email_validator
from .service import UserService

user_fields = {
    "id": fields.Integer,
    "email": fields.String,
}
parser = reqparse.RequestParser()
parser.add_argument(
    "email", type=email_validator, required=True, help="A valid email is required"
)
parser.add_argument(
    "password",
    type=str,
    required=True,
    help="Password is required",
)


class UsersResource(Resource):
    def get(self):
        users = UserService.get_all_users()
        return {
            "code": 200,
            "message": "Success",
            "data": marshal(users, user_fields),
        }, 200

    def post(self):
        args = parser.parse_args()
        username = args["email"]
        password = args["password"]
        user, error_code, message = UserService.create_user(username, password)

        if error_code is not None:
            return {"message": message}, error_code

        return {
            "code": 201,
            "message": "Created",
            "data": marshal(user, user_fields),
        }, 201


class UserResource(Resource):
    def get(self, user_id):
        return {"hello": user_id}


class UserProfileResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user, error_code, message = UserService.get_user_by_id(user_id)
        if error_code is not None:
            return {"message": message}, error_code
        return {
            "code": 200,
            "message": "Success",
            "data": marshal(user, user_fields),
        }, 200
