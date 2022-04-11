#!/usr/bin/python3
"""print first State object from the database hbtn_0e_6_usa"""

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

    """fetch first State obj in states.id"""
    first_obj = session.query(State).order_by(State.id).first()

    """display State object"""
    if first_obj:
        print("{}: {}".format(first_obj.id, first_obj.name))
    else:
        print("Nothing")

    """close session"""
    session.close()
