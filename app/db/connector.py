import logging
import os

from dotenv import load_dotenv
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

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


# def get_session() -> Session:
#     session = sessionmaker(bind=_engine)
#     with session() as s:
#         yield s


def init_db() -> None:
    SQLModel.metadata.create_all(bind=_engine)


LocalSession = sessionmaker(bind=_engine)
