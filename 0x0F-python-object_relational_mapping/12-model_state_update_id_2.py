#!/usr/bin/python3
"""changes name of State object from the database hbtn_0e_6_usa"""

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

    """change name of State object"""
    new_name = session.query(State).filter(State.id == 2).first()
    new_name.name = "New Mexico"
    session.commit()

    """close session"""
    session.close()
