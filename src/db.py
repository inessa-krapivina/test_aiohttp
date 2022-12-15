from contextlib import contextmanager

from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    login = Column(String)
    password = Column(String)
    date_of_birth = Column(String)
    is_superuser = Column(Boolean, default=False)


engine = create_engine(
    "postgresql+psycopg2://admin:123123@5432/db"
    # "sqlite:///database.db"
)


Base.metadata.create_all(engine)


@contextmanager
def db_session():
    connection = engine.connect()
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=True, bind=engine)
    )
    yield db_session
    db_session.close()
    connection.close()


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


def create_user(name: str, lastname: str, login: str, passwd: str, date_of_birth: str):
    with db_session() as session:
        user = Users(
            name=name,
            lastname=lastname,
            login=login,
            passwd=passwd,
            date_of_birth=date_of_birth,
        )
        session.add(user)
        session.commit()


def read_users():
    result = []
    with db_session() as session:
        users = session.query(Users).all()
        for user in users:
            result.append(row2dict(user))
    return result


def update_user_in_db(old_name: str, new_name: str):
    with db_session() as session:
        session.query(Users).filter(Users.name == old_name).update(
            {Users.name: new_name}
        )
        session.commit()


def delete_user(name: str):
    with db_session() as session:
        user = session.query(Users).filter(Users.name == name).one()
        session.delete(user)
        session.commit()


# create_user(name='name', lastname='lastname', login='admin', password='admin', date_of_birth='11.11.1111')
# update_user_in_db(old_name='name', new_name='nameTEST')
# delete_user(name='name2')
# read_users()
