import csv
import os
from flask import Flask, render_template, request, url_for, redirect, session # gives access to a variable called `session`
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/flights")
 def flights():
     flights = db.execute("SELECT * FROM flights").fetchall()
     return render_template("flights.html", flights=flights)

 @app.route("/flights/<int:flight_id>")
 def flight(flight_id):
     # Make sure flight exists.
     flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
     if flight is None:
         return render_template("error.html", message="No such flight.")

     # Get all passengers.
     passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                             {"flight_id": flight_id}).fetchall()
     return render_template("flight.html", flight=flight, passengers=passengers)
