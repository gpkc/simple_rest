from apispec import APISpec
from flask import Flask
from flask_apispec import FlaskApiSpec, marshal_with
from flask_cors import CORS

from schemas import ErrorSchema


# Create app
app = Flask(__name__)

app.config['APISPEC_SPEC'] = APISpec(
    title='simple_rest',
    version='v1',
    plugins=('apispec.ext.marshmallow', ))
app.config['APISPEC_SWAGGER_URL'] = '/swagger/'


# Register views

# from .views import ...
# app.add_url_rule('<route>', view_func=<myview>.as_view('<viewname>'))
# ...

# Register view on apispec
docs = FlaskApiSpec(app)

# docs.register(<myview>)
# ...


# Register RESTful error handler
@app.errorhandler(404)
@marshal_with(ErrorSchema, code=404)
def handle_not_found(err):
    exc = getattr(err, 'description')
    if exc:
        message = err.description
    else:
        message = ['Not found']
    return {
        'status': 'fail',
        'message': message
    }, 404


# Enable CORS
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
