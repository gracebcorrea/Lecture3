import csv
import os
from flask import Flask, render_template, request, url_for, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = creage_engine(os.getenv("DATABASE_URL"))
db =scoped_session(sessionmaker(bind=engine))

  # same import and setup statements as above
def main():
    #list all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flight "),fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes")

    #Prompt user to choose a flight.
    flight_id = int(input("\nFlight ID:"))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id ", )
                        {"id": flight_id}).fetchone()

    #make sure the flight is valid
    if flight is None:
        print("Error: No such flight.")
        return

    #List passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == o:
        print("no passengers.")
