from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


@contextmanager
def session_scope():
    engine = create_engine(
        url="mysql+pymysql://admin:oliver37632@database-1.cj4qlua9nvsk.ap-northeast-2.rds.amazonaws.com:3306/neonadeuli",
        encoding="utf-8"
    )
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

Base = declarative_base()
