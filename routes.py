from flask_restful import Api
from modules.users.resource import UsersResource, UserResource, UserProfileResource
from modules.auth.resource import SignInResource, RefreshTokenResource


def register_resources(api: Api):
    api.add_resource(UsersResource, "/users")
    api.add_resource(UserProfileResource, "/users/me")
    api.add_resource(UserResource, "/users/<user_id>")
    api.add_resource(SignInResource, "/auth/sign-in")
    api.add_resource(RefreshTokenResource, "/auth/refresh")
