# TODO: Feature 3
from app import app

def test_get_movie_by_title():
    with app.test_client() as client:
        response = client.get('/movies/search?q=The%20Shawshank%20Redemption')
        assert response.status_code == 200
        assert b'The Shawshank Redemption' in response.data
