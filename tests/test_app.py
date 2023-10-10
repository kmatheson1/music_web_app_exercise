"""
When I POST /albums with album info
It is reflected in the list returned by GET albums
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post('/albums', data={
        'title': 'Bleach',
        'release_year': '1989',
        'artist_id': '2'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
            "Album(1, Californication, 1999, 1)\n" \
            "Album(2, Nevermind, 1991, 2)\n" \
            "Album(3, In Utero, 1993, 2)\n" \
            "Album(4, Ten, 1991, 3)\n" \
            "Album(5, By the Way, 2002, 1)\n" \
            "Album(6, Bleach, 1989, 2)"

def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "" \
        "Title, release_year, artist_id must be submitted"

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
            "Album(1, Californication, 1999, 1)\n" \
            "Album(2, Nevermind, 1991, 2)\n" \
            "Album(3, In Utero, 1993, 2)\n" \
            "Album(4, Ten, 1991, 3)\n" \
            "Album(5, By the Way, 2002, 1)"

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Red Hot Chili Peppers, Nirvana, Pearl Jam"
    
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post('/artists', data={
        'name': 'Foo Fighters',
        'genre': 'Rock',
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Red Hot Chili Peppers, Nirvana, Pearl Jam, Foo Fighters"

def test_post_albums_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post('/artists')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Name, Genre must be submitted'

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Red Hot Chili Peppers, Nirvana, Pearl Jam"