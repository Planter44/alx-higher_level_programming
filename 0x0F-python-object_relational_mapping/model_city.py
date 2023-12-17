#!/usr/bin/python3
"""
This script defines a City class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from relationship_state import Base

class City(Base):
    """class links
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
