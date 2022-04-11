#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """create engine to connect to database using log in sent as arguments"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
             argv[1], argv[2], argv[3]))

    """create a session to talk to the database"""
    session = sessionmaker(bind=engine)()

    """store City objects in var"""
    results = session.query(City, State).join(State)

    """display City objects and corresponding state"""
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    """close session"""
    session.close()
