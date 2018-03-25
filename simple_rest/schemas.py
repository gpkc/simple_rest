from marshmallow import fields, Schema


class UserSchema(Schema):
    pass


class UserResponseSchema(Schema):
    pass


class UsersResponseSchema(Schema):
    pass


class ErrorSchema(Schema):
    status = fields.String()
    message = fields.String()
