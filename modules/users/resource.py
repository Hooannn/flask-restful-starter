from flask_restful import Resource, fields, marshal
from .service import *

user_fields = {
    "id": fields.Integer,
    "email": fields.String,
}


class UsersResource(Resource):
    def get(self):
        users = get_all_users()
        return {
            "code": 200,
            "message": "Success",
            "data": marshal(users, user_fields),
        }, 200

    def post(self):
        return {"hello": "world"}


class UserResource(Resource):
    def get(self, user_id):
        return {"hello": user_id}

    def put(self, user_id):
        return {"hello": user_id}

    def delete(self, user_id):
        return {"hello": user_id}
