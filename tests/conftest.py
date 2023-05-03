import pytest
from app import create_app, db
from app.models.planet import Planet
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app(True)

    @request_finished.connect_via(app)
    def expire_session(slender,response, **extra):
        db.session.remove()
        
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets():
    saturn = Planet(name="Saturn", description="Sixth planet from sun", number_of_moons= 83)
    neptune = Planet(name="Neptune", description="is blue", number_of_moons=14)

    db.session.add_all([saturn,neptune])
    db.session.commit()