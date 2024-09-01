from flask_restful import Api
from modules.users.resource import UsersResource, UserResource

def register_resources(api: Api):
    api.add_resource(UsersResource, '/users')
    api.add_resource(UserResource, '/users/<user_id>')