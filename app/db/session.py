from sqlmodel import create_engine, Session
from app.core.config import config


# Sin volumenes:
# "sqlite:///./database.db"

#con volumen:
db_url = config.database_url or "sqlite:///./data/database.db"


is_sqlite = db_url.startswith("sqlite")
connect_args = {"check_same_thread": False} if is_sqlite else {}

engine = create_engine(
    db_url,
    echo=config.debug,
    connect_args=connect_args
)

def get_session():
    with Session(engine) as session:
        yield session