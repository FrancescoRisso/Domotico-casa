from mysql.connector import Error


# Insert a certain temperature in the database
def insert(value, source, writer, date):
    try:
        writer.execute("INSERT INTO CONSUMPTIONS(Date, Consumption, InputID) VALUES('" + date + "', " + str(value) + ", " + str(source) + ")")
        writer.execute("UPDATE CURRENT_CONSUMPTIONS SET Consumption = " + str(value) + " WHERE InputID = " + str(source))

    except Error as e:
        print("Error while putting data in the database: '"+ str(e) + "'")
