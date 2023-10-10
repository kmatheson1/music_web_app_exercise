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

GET artists/

POST artists/
    name: str
    genre: str


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

# Example 3
    # GET /artists
    # Expected response: (200 OK)
    """
    Red Hot Chili Peppers, Nirvanna, Pearl Jam
    """

# Example 4
    # POST /artists
    #     name: Foo Fighters
    #     genre: Rock
    # Expected response: (200 OK)
    """(no content)
    """

    # GET /artists
    # Expected response: (200 OK)
    """
    Red Hot Chili Peppers, Nirvanna, Pearl Jam, Foo Fighters
    """

    # EXAMPLE 2
    # POST /albums
    # Expected response: (400 Bad Request)
    """
    Name, Genre must be submitted
    """

    # GET /albums
    # Expected response: (200 OK)
    """
    Red Hot Chili Peppers, Nirvanna, Pearl Jam
    """

```

## 3. Test-drive the Route

*After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.*

Here's an example for you to start with:

```python
```