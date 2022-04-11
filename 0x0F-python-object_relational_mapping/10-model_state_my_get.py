#!/usr/bin/python3
"""list prints State obj with name passed as arg from database hbtn_0e_6_usa"""

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

    """search state name and store it in var"""
    state_name = session.query(State).filter(State.name == argv[4]).first()

    """display State object"""
    if state_name:
        print(state_name.id)
    else:
        print("Not found")

    """close session"""
    session.close()
