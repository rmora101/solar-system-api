import pytest

def test_get_all_planets(client, two_planets):
    response = client.get("/planets")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id":1,
        "name":"Saturn", 
        "description":"Sixth planet from sun", 
        "number_of_moons": 83
    },
    {
        "id":2,
        "name":"Neptune", 
        "description":"is blue", 
        "number_of_moons":14
    }]

def test_get_planet_by_id(client, two_planets):
    response = client.get("/planets/1")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name":"Saturn", 
        "description":"Sixth planet from sun", 
        "number_of_moons": 83
    }

def test_no_data_returns_404(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

def test_post_adds_planet(client):

    response = client.post("/planets", json={
        "name": "Mercury",
        "description": "Hot",
        "number_of_moons": 0
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body


    