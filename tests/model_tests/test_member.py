from app import db
from app.models import Member

def test_member_data(test_client, test_member):
    assert test_member.username == 'member'
    assert test_member.check_password('test')
    assert test_member.role == 'member'
    assert test_member.bio is None
    assert test_member.registration_date is not None
    # assert test_member.api_tokens == []

def test_mod_data(test_client, test_mod):
    assert test_mod.username == 'mod'
    assert test_mod.check_password('test')
    assert test_mod.role == 'mod'
    assert test_mod.bio is None
    assert test_mod.registration_date is not None
    # assert test_member.api_tokens == []

def test_admin_data(test_client, test_admin):
    assert test_admin.username == 'admin'
    assert test_admin.check_password('test')
    assert test_admin.role == 'admin'
    assert test_admin.bio is None
    assert test_admin.registration_date is not None
    # assert test_member.api_tokens == []

    