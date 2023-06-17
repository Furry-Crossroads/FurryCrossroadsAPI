from base64 import b64encode

"""This should mostly act like an external script making requests to the API to test it.
"""

def test_get(test_client, test_member):
    member = b64encode(f"{test_member.username}:test".encode()).decode('utf-8')

    response = test_client.get('/member', headers={'Authorization': 'Basic ' + member})

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json["username"] == test_member.username
    print(response.json)