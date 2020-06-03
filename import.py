import csv

  # same import and setup statements as above

  f = open("flights.csv")
  reader = csv.reader(f)
  for origin, destination, duration in reader: # loop gives each column a name
      db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                  {"origin": origin, "destination": destination, "duration": duration}) # substitute values from CSV line into SQL command, as per this dict
      print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
  db.commit() # transactions are assumed, so close the transaction finished
