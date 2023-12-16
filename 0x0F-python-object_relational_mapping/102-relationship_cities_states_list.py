#!/usr/bin/python3
"""
The script lists all city objects.
"""

import sys
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(bind=engine)
    cities = session.query(City)

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
