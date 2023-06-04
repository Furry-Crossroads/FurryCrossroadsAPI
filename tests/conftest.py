import pytest
from datetime import datetime, timedelta
from base64 import b64encode

from app import app, db
from app.models import Member, ApiToken


# So this is needed in all of the tests. You must have it
# as a parameter so that the test/fixture can get app context.
@pytest.fixture
def test_client():
    app.config.update(
        TESTING=True, 
        FCAPI_SQLALCHEMY_DATABASE_NAME='testdb',
    )
    with app.app_context():
        db.create_all()
        with app.test_client() as client:
            yield client

    

@pytest.fixture
def test_admin(test_client):
    member = Member.query.filter_by(username='admin').first()
    if member: 
        return member
    member = Member(
        username='admin',
        role='admin',
    )
    member.set_password('test')
    db.session.add(member)
    db.session.commit()
    return member

@pytest.fixture
def test_mod(test_client):
    member = Member.query.filter_by(username='mod').first()
    if member: 
        return member
    member = Member(
        username='mod',
        role='mod',
    )
    member.set_password('test')
    db.session.add(member)
    db.session.commit()
    return member

@pytest.fixture
def test_member(test_client):
    member = Member.query.filter_by(username='member').first()
    if member: 
        return member
    member = Member(
        username='member',
        role='member',
    )
    member.set_password('test')
    db.session.add(member)
    db.session.commit()
    return member

@pytest.fixture
def empty(test_client, test_member, test_admin, test_mod):
    """Just here to spawn all the members.
    """
    ...