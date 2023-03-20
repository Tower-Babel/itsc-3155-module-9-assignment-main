# TODO: Feature 1
from app import app

def test_get_all_movies():
    with app.test_client() as client:
        response = client.get('/movies')
        assert response.status_code == 200
        assert b'All Movies' in response.data
