from typing import Generator
from app.db.connector import get_session


def get_db() -> Generator:
    """call this to get a Session object for use for execution of
    db requests"""
    try:
        session = get_session()
        yield session
    finally:
        session.close()
