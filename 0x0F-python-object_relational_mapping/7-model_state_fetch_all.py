#!/usr/bin/python3
"""
The script lists all state objects from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    data_A = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(data_A)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
