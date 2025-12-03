from sqlmodel import Field, Session, SQLModel, create_engine, select


# Database configuration
DATABASE_NAME = "top_rates.db"
sqlite_url = f"sqlite:///{DATABASE_NAME}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session