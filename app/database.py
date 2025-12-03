from sqlmodel import Field, Session, SQLModel, create_engine, select


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


# Database configuration
DATABASE_NAME = "top_rates.db"
sqlite_url = f"sqlite:///{DATABASE_NAME}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


def get_session():
    with Session(engine) as session:
        yield session