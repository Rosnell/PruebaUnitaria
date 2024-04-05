# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


# test_app.py
from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert b'Hello, World!' in rv.data



