#!/usr/bin/python3
"""
The script lists all state objects from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()
    for row in s.query(State).order_by(State.id.asc()):
        print(row.id, end="")
        print(': ', end="")
        print(row.name)
