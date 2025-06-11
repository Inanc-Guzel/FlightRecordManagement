import sqlite3

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database

class DBOperations:
    sql_create_table_firsttime = "CREATE TABLE IF NOT EXISTS FlightInfo (FlightID INTEGER PRIMARY KEY, FlightOrigin TEXT, FlightDestination TEXT, Status TEXT)"
    
    sql_create_table = "CREATE TABLE FlightInfo (FlightID INTEGER PRIMARY KEY, FlightOrigin TEXT, FlightDestination TEXT, Status TEXT)"
    
    sql_insert = "INSERT INTO FlightInfo (FlightID, FlightOrigin, FlightDestination, Status) VALUES (?, ?, ?, ?)"
    sql_select_all = "SELECT * FROM FlightInfo"
    sql_search = "SELECT * FROM FlightInfo WHERE FlightID = ?"
    sql_update_data = "UPDATE FlightInfo SET FlightOrigin = ?, FlightDestination = ?, Status = ? WHERE FlightID = ?"
    sql_delete_data = "DELETE FROM FlightInfo WHERE FlightID = ?"
    sql_drop_table = "DROP TABLE IF EXISTS FlightInfo"

    def __init__(self):
        try:
            self.conn = sqlite3.connect("FlightDatabase.db")
            self.cur = self.conn.cursor()
            self.cur.execute(self.sql_create_table_firsttime)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def get_connection(self):
        self.conn = sqlite3.connect("FlightDatabase.db")
        self.cur = self.conn.cursor()

    def create_table(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_create_table)
            self.conn.commit()
            print("Table created successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def insert_data(self):
        try:
            self.get_connection()
            
            flight = FlightInfo()
            flight.set_flight_id(int(input("Enter FlightID: ")))
            flight.set_flight_origin(input("Enter Flight Origin: "))
            flight.set_flight_destination(input("Enter Flight Destination: "))
            flight.set_status(input("Enter Status: "))
            
            self.cur.execute(self.sql_insert, (flight.get_flight_id(), 
                                             flight.get_flight_origin(), 
                                             flight.get_flight_destination(), 
                                             flight.get_status()))
            
            self.conn.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def select_all(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_all)
            result = self.cur.fetchall()
            
            if result:
                print("\n--- All Flight Records ---")
                for row in result:
                    print(f"Flight ID: {row[0]}")
                    print(f"Origin: {row[1]}")
                    print(f"Destination: {row[2]}")
                    print(f"Status: {row[3]}")
                    print("-" * 25)
            else:
                print("No records found")
                
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def search_data(self):
        try:
            self.get_connection()
            flightID = int(input("Enter FlightNo: "))
            self.cur.execute(self.sql_search, (flightID,))
            result = self.cur.fetchone()
            if result:
                print("Flight ID: " + str(result[0]))
                print("Flight Origin: " + result[1])
                print("Flight Destination: " + result[2])
                print("Status: " + str(result[3]))
            else:
                print("No Record")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def update_data(self):
        try:
            self.get_connection()
            
            flightID = int(input("Enter FlightID to update: "))
            new_origin = input("Enter new Flight Origin: ")
            new_destination = input("Enter new Flight Destination: ")
            new_status = input("Enter new Status: ")
            
            result = self.cur.execute(self.sql_update_data, (new_origin, new_destination, new_status, flightID))
            self.conn.commit()
            
            if result.rowcount != 0:
                print(str(result.rowcount) + " Row(s) affected.")
            else:
                print("Cannot find this record in the database")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def delete_data(self):
        try:
            self.get_connection()
            
            flightID = int(input("Enter FlightID to delete: "))
            result = self.cur.execute(self.sql_delete_data, (flightID,))
            self.conn.commit()
            
            if result.rowcount != 0:
                print(str(result.rowcount) + " Row(s) affected.")
            else:
                print("Cannot find this record in the database")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


class FlightInfo:

    def __init__(self):
        self.flightID = 0
        self.flightOrigin = ''
        self.flightDestination = ''
        self.status = ''

    def set_flight_id(self, flightID):
        self.flightID = flightID

    def set_flight_origin(self, flightOrigin):
        self.flightOrigin = flightOrigin

    def set_flight_destination(self, flightDestination):
        self.flightDestination = flightDestination

    def set_status(self, status):
        self.status = status

    def get_flight_id(self):
        return self.flightID

    def get_flight_origin(self):
        return self.flightOrigin

    def get_flight_destination(self):
        return self.flightDestination

    def get_status(self):
        return self.status

    def __str__(self):
        return str(self.flightID) + "\n" + self.flightOrigin + "\n" + self.flightDestination + "\n" + str(self.status)


# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

if __name__ == "__main__":
    while True:
        print("\n Menu:")
        print("**********")
        print(" 1. Create table FlightInfo")
        print(" 2. Insert data into FlightInfo")
        print(" 3. Select all data from FlightInfo")
        print(" 4. Search a flight")
        print(" 5. Update data some records")
        print(" 6. Delete data some records")
        print(" 7. Exit\n")

        __choose_menu = int(input("Enter your choice: "))
        db_ops = DBOperations()
        if __choose_menu == 1:
            db_ops.create_table()
        elif __choose_menu == 2:
            db_ops.insert_data()
        elif __choose_menu == 3:
            db_ops.select_all()
        elif __choose_menu == 4:
            db_ops.search_data()
        elif __choose_menu == 5:
            db_ops.update_data()
        elif __choose_menu == 6:
            db_ops.delete_data()
        elif __choose_menu == 7:
            exit(0)
        else:
            print("Invalid Choice")