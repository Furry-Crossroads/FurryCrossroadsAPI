from base64 import b64encode

def test_token_gen_post(test_client, test_member, test_mod, test_admin):
    """Try to generate a token for each member
    """
    member = b64encode(f"{test_member.username}:test".encode()).decode('utf-8')
    mod = b64encode(f"{test_mod.username}:test".encode()).decode('utf-8')
    admin = b64encode(f"{test_admin.username}:test".encode()).decode('utf-8')

    response = test_client.post('/token', headers={'Authorization': 'Basic ' + member})
    assert response.status_code == 201
    assert 'token' in response.get_json()

    response = test_client.post('/token', headers={'Authorization': 'Basic ' + mod})
    assert response.status_code == 201
    assert 'token' in response.get_json()

    response = test_client.post('/token', headers={'Authorization': 'Basic ' + admin})
    assert response.status_code == 201
    assert 'token' in response.get_json()

def test_token_gen_delete(test_client, test_member, test_mod, test_admin):
    # Get the most recent token
    member_token = test_member.api_tokens[-1].token
    mod_token = test_mod.api_tokens[-1].token
    admin_token = test_admin.api_tokens[-1].token

    response = test_client.delete('/token', headers={'Authorization': 'Bearer ' + member_token})
    assert response.status_code == 204

    response = test_client.delete('/token', headers={'Authorization': 'Bearer ' + mod_token})
    assert response.status_code == 204

    response = test_client.delete('/token', headers={'Authorization': 'Bearer ' + admin_token})
    assert response.status_code == 204

    # Then test that the tokens are atually deleted.
    