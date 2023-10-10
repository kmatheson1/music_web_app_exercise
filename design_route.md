## POST/ Albums Route Design Recipe

*Copy this design recipe template to test-drive a plain-text Flask route.*

## 1. Design the Route Signature

*Include the HTTP method, the path, and any query or body parameters.*

```markdown

POST albums/
    title: str
    release_year: number (str)
    artist_id: number (str)

GET albums/

```

## 2. Create Examples as Tests

*Go through each route and write down one or more example responses.*

*Remember to try out different parameter values.*

*Include the status code and the response body.*

```python
# EXAMPLE 1
    # POST /albums
    #     title: 'Bleach'
    #     release_year: 1989
    #     artist_id: 2
    # Expected response: (200 OK)
    """
    """(no content)

    # GET /albums
    # Expected response: (200 OK)
    """
    Album(1, 'Californication',1999, 1)
    Album(2, 'Nevermind', 1991, 2)
    Album(3, 'In Utero', 1993, 2)
    Album(4, 'Ten', 1991, 3)
    Album(5, 'By the Way', 2002, 1)
    Album(6, 'Bleach', 1989, 2)
    """

# EXAMPLE 2
    # POST /albums
    # Expected response: (400 Bad Request)
    """
    Title, release_year, artist_id must be submitted
    """(no content)

    # GET /albums
    # Expected response: (200 OK)
    """
    Album(1, 'Californication',1999, 1)
    Album(2, 'Nevermind', 1991, 2)
    Album(3, 'In Utero', 1993, 2)
    Album(4, 'Ten', 1991, 3)
    Album(5, 'By the Way', 2002, 1)
    """

```

## 3. Test-drive the Route

*After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.*

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```