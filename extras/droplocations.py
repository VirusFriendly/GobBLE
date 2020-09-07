import sqlite3
import sys

def droplocations(db):
    #Connecting to sqlite
    conn = sqlite3.connect(db)
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Doping EMPLOYEE table if already exists
    cursor.execute("DROP TABLE locations")
    print("Locations dropped... ")
    #Commit your changes in the database
    conn.commit()
    #Closing the connection
    conn.close()

if __name__ == "__main__":
    db = "RaMBLE.sqlite"

    if len(sys.argv) > 1:
        print(sys.argv)
        db = sys.argv[1]

    droplocations(db)
