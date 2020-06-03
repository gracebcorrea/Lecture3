import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = creage_engine(os.getenv("DATABASE_URL"))
db =scoped_session(sessionmaker(bind=engine))

  # same import and setup statements as above
def main():
    #list all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flight ")
    for flight in flights:
        print("Flight {flight,db}: {flight.origin} to {flight.destination},")

    #Prompt user to choose a flight.
    flight_id = int(input("\nFlight ID:"))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE ")
                        {"id": flight_id}).fetchone()
