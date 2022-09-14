import os
import logging
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.engine import Engine
from dotenv import load_dotenv

_log = logging.getLogger(__name__)
load_dotenv()

SQLITE_FILE = os.environ.get("SQLITE_FILE", "")


# TODO: update this to simply store the full url in .env
def get_engine() -> Engine:
    sqlite_url = f"sqlite:///{SQLITE_FILE}"
    options = {"check_same_thread": False}
    try:
        engine = create_engine(sqlite_url, echo=True, connect_args=options)
    except (EnvironmentError, Exception) as err:
        _log.exception("problem connecting to database with url %s", sqlite_url)
        print(f"uh oh bucko {err}")
        raise

    return engine


_engine = get_engine()


def get_session() -> Session:
    with Session(bind=_engine) as session:
        yield session


def init_db() -> None:
    SQLModel.metadata.create_all(bind=_engine)
