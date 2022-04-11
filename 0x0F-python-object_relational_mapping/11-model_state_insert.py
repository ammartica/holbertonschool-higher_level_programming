#!/usr/bin/python3
"""adds State object "Louisiana" to database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """create engine to connect to database using log in sent as arguments"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
             argv[1], argv[2], argv[3]))

    """create a session to talk to the database"""
    session = sessionmaker(bind=engine)()

    """create Louisiana State object"""
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    """display Louisiana object id"""
    print(louisiana.id)

    """close session"""
    session.close()
