from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal


class UsersResource(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}
    
class UserResource(Resource):
    def get(self, user_id):
        return {'hello': user_id}

    def put(self, user_id):
        return {'hello': user_id}

    def delete(self, user_id):
        return {'hello': user_id}