from flask_restful import Resource, fields, marshal, reqparse
from flask_jwt_extended import decode_token
from .service import AuthService
from utils import email_validator

user_fields = {
    "id": fields.Integer,
    "email": fields.String,
}


class SignInResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "email",
            type=email_validator,
            required=True,
            help="A valid email is required",
        )
        parser.add_argument(
            "password",
            type=str,
            required=True,
            help="Password is required",
        )
        args = parser.parse_args()
        username = args["email"]
        password = args["password"]

        data, error_code, message = AuthService.sign_in(username, password)

        if error_code is not None:
            return {"message": message}, error_code

        return {
            "code": 200,
            "message": "Signed in successfully",
            "data": {
                "user": marshal(data["user"], user_fields),
                "credentials": data["credentials"],
            },
        }, 200


class RefreshTokenResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "refresh_token", type=str, required=True, help="Refresh token is required"
        )
        args = parser.parse_args()
        refresh_token = args["refresh_token"]

        decoded_token = decode_token(refresh_token)
        user_id = decoded_token["sub"]
        data, error_code, message = AuthService.refresh_token(user_id, refresh_token)

        if error_code is not None:
            return {"message": message}, error_code

        return {
            "code": 200,
            "message": "Token refreshed successfully",
            "data": data,
        }, 200
