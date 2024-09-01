from datetime import timedelta

SQLALCHEMY_DATABASE_URI = "postgresql://class_management_owner:mxI0BkvhPgN2@ep-young-brook-a1fnwp3h.ap-southeast-1.aws.neon.tech/class_management?sslmode=require"
SQLALCHEMY_TRACK_MODIFICATIONS = False
BUNDLE_ERRORS = True
JWT_SECRET_KEY = "3j4k5h43kj5hj234b5jh34bk25b5k234j5bk2j3b532"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
