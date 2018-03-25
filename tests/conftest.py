import json

import pytest

from store import store


@pytest.fixture
def app():
    from app import app as app_
    ctx = app_.test_request_context()
    ctx.push()

    yield app_

    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True, scope='function')
def setup_db(app):
    # create_all step for a real database
    yield
    store.clear()


@pytest.fixture
def send_request(client):
    def send_request_(endpoint, method, headers=None, **kwargs):
        if not headers:
            headers = {}
        response = getattr(client, method)(
            endpoint,
            data=json.dumps(dict(**kwargs)),
            content_type='application/json',
            headers=headers
        )
        if response.data:
            data = json.loads(response.data.decode())
        else:
            data = {}
        return response, data
    return send_request_


@pytest.fixture
def post_user(send_request):
    pass


@pytest.fixture
def get_user(send_request):
    pass


@pytest.fixture
def put_user(send_request):
    pass


@pytest.fixture
def delete_user(send_request):
    pass
