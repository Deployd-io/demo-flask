"""Scope probe for the 19 Nov QA retest: the three shapes that produced NameError logs."""
import sqlite3
import time
import logging
logger = logging.getLogger(__name__)


def reference_col(tablename, nullable=False, pk_name="id"):
    """A foreign key column.

    Usage: ::

        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    logger.error(">>> Entering reference_col(tablename=%s,nullable=%s,pk_name=%s)", tablename, nullable, pk_name, extra={"event.action": "reference_col", "logrite.tablename": tablename, "logrite.nullable": nullable, "logrite.pk_name": pk_name})
    logger.warning("<<< Exiting reference_col(tablename=%s,nullable=%s,pk_name=%s)", tablename, nullable, pk_name, extra={"event.action": "reference_col", "logrite.tablename": tablename, "logrite.nullable": nullable, "logrite.pk_name": pk_name})
    return (tablename, nullable, pk_name)


def fetch_rows(conn):
    """Read one row, so the database rule asks for a timer."""
    logger.error(">>> Entering fetch_rows(conn=%s)", conn, extra={"event.action": "fetch_rows"})
    __log_start = time.time()
    cursor = conn.execute("select 1")
    logger.error("fetch_rows(conn)=%s: find operation took %s ms", conn, int((time.time() - __log_start) * 1000), extra={"event.action": "fetch_rows", "event.category": "database"})
    logger.error("fetch_rows(conn=%s): cursor → %s", conn, cursor, extra={"event.action": "fetch_rows"})
    rows = cursor.fetchall()
    logger.error("fetch_rows(conn=%s): rows → %s", conn, rows, extra={"event.action": "fetch_rows"})
    logger.warning("<<< Exiting fetch_rows(conn=%s)", conn, extra={"event.action": "fetch_rows"})
    return rows


def open_store(path):
    logger.error(">>> Entering open_store(path=%s)", path, extra={"event.action": "open_store", "logrite.path": path})
    connection = sqlite3.connect(path)
    logger.error("open_store(path=%s): connection → %s", path, connection, extra={"event.action": "open_store", "logrite.path": path})
    logger.warning("<<< Exiting open_store(path=%s)", path, extra={"event.action": "open_store", "logrite.path": path})
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
        logger.error(">>> Entering __init__(username=%s,email=<redacted>,password=<redacted>)", username, extra={"event.action": "__init__", "user.name": str(username)})
        self.username = username
        logger.debug("__init__(self=%s,username=%s,email=<redacted>,password=<redacted>): self.username → %s", self, username, self.username, extra={"event.action": "__init__", "user.name": str(username)})
        logger.error("__init__(username=%s,email=<redacted>,password=<redacted>): self.username → %s", username, self.username, extra={"event.action": "__init__", "user.name": str(username)})
        self.email = email
        self.password_hash = password + "-hashed"
        logger.error("__init__(username=%s,email=<redacted>,password=<redacted>): self.email → <redacted>", username, extra={"event.action": "__init__", "user.name": str(username)})
        logger.debug("__init__(self=%s,username=%s,email=<redacted>,password=<redacted>): self.email → <redacted>", self, username, extra={"event.action": "__init__", "user.name": str(username)})

    def set_password(self, password):
        logger.error(">>> Entering set_password(password=<redacted>)", extra={"event.action": "set_password"})
        self.password_hash = password + "-hashed"
        logger.error("set_password(password=<redacted>): self.password_hash → <redacted>", extra={"event.action": "set_password"})
        logger.warning("<<< Exiting set_password(password=<redacted>)", extra={"event.action": "set_password"})

    def check_password(self, value):
        logger.error(">>> Entering check_password(value=<redacted>)", extra={"event.action": "check_password"})
        logger.warning("<<< Exiting check_password(value=<redacted>)", extra={"event.action": "check_password"})
        return self.password_hash == value + "-hashed"

    @property
    def bio(self):
        return self._bio
