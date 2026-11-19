"""Scope probe for the 19 Nov QA retest: the three shapes that produced NameError logs."""
import sqlite3


def reference_col(tablename, nullable=False, pk_name="id"):
    """A foreign key column.

    Usage: ::

        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    return (tablename, nullable, pk_name)


def fetch_rows(conn):
    """Read one row, so the database rule asks for a timer."""
    cursor = conn.execute("select 1")
    rows = cursor.fetchall()
    return rows


def open_store(path):
    connection = sqlite3.connect(path)
    return connection


class Article:
    def __init__(self, author, title, body, description, slug):
        self.author = author
        self.title = title
        self.body = body
        self.description = description
        self.slug = slug


class Tags:
    def __init__(self, tagname):
        self.tagname = tagname


class Comment:
    def __init__(self, body, author):
        self.body = body
        self.author = author


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password + "-hashed"

    def set_password(self, password):
        self.password_hash = password + "-hashed"

    def check_password(self, value):
        return self.password_hash == value + "-hashed"

    @property
    def bio(self):
        return self._bio
