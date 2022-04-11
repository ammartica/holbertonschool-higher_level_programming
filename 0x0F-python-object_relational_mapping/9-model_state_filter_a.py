#!/usr/bin/python3
"""list all State objs with letter a from the database hbtn_0e_6_usa"""

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

    """store state objs with a in asc order by states.id in results var"""
    results = session.query(State).filter(State.name.contains('a'))

    """display State objects"""
    for state in results:
        print("{}: {}".format(state.id, state.name))

    """close session"""
    session.close()
