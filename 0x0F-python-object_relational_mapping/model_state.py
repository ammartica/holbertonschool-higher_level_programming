#!/usr/bin/python3
"""Contains class State and instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Child class inherits from Base and defines a State"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
