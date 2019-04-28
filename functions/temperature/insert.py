from mysql.connector import Error


# Insert a certain temperature in the database
def insert_temp(value, source, writer, date):
    try:
        writer.execute("INSERT INTO DATA(Date, Temperature, InputID) VALUES('" + date + "', " + str(value) + ", " + source + ")")
        writer.execute("UPDATE CURRENT_DATA SET Temperature = " + str(value) + " WHERE InputID = " + source)

    except Error as e:
        print("Error while putting data in the database")
        print(e)
        raise Exception("Writing to the db")
