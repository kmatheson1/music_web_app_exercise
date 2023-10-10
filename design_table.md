# Single Table Design Recipe Template

*Copy this recipe template to design and create a database table from a specification.*

## 1. Extract nouns from the user stories or specification

```markdown
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

    # Request:
    POST /albums

    # With body parameters:
    title=Voyage
    release_year=2022
    artist_id=2

    # Expected response (200 OK)
    (No content)
```

```markdown
Nouns:

album, title, release year, artist, id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record | Properties |
| ------ | ---------- |
| album  | title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`

## 3. Decide the column types

```markdown
# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int

```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int
  artist_id int
);
```

## 5. Create the table
