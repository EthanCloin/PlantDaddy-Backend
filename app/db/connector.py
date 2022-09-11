import os
import logging
from sqlmodel import create_engine, SQLModel
from sqlmodel.engine import Engine
from dotenv import load_dotenv

_log = logging.getLogger(__name__)
load_dotenv()

SQLITE_FILE = os.environ.get("SQLITE_FILE", "")


def create_tables(engine: Engine):
    SQLModel.metadata.create_all(bind=engine)


def get_engine() -> Engine:
    """"""
    sqlite_url = f"sqlite:///{SQLITE_FILE}"
    options = {"check_same_thread": False}
    try:
        engine = create_engine(sqlite_url, echo=True, connect_args=options)
    except (EnvironmentError, Exception) as err:
        _log.exception("problem connecting to database with url %s", sqlite_url)
        print(f"uh oh bucko {err}")
        raise

    # looks at models which are tagged with "table=True"
    # and links them to the tables
    create_tables(engine=engine)
    return engine
