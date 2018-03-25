from webargs import fields, ValidationError


def validate_age(age):
    if age < 0:
        raise ValidationError('Age must be greater than 0.')
