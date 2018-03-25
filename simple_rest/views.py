from flask_apispec import MethodResource, use_kwargs, doc, marshal_with
from webargs import fields, ValidationError
from flask import abort


class UserView(MethodResource):
    pass


class UsersView(MethodResource):
    pass
