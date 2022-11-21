from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


postresql = {
    "username": "nobora",
    "password": "coolpass123",
    "host": "127.0.0.1",
    "port": 5432,
    "db_name": "orm_test"
}


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_engine_from_settings(settings):
    keys = ["username", "password", "host", "port", "db_name"]
    if not all(key in keys for key in settings.keys()):
        raise Exception("Bad config file")

    return get_engine(settings["username"],
                      settings["password"],
                      settings["host"],
                      settings["port"],
                      settings["db_name"],)


def get_session(settings=postresql):
    engine = get_engine_from_settings(settings)
    session = sessionmaker(bind=engine)
    return session


session = get_session(postresql)
