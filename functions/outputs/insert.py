from mysql.connector import Error


# Insert a certain output in the database
def insert_out(value, source, writer, date):
    try:
        writer.execute("INSERT INTO OUTPUTS_DATA(State, Date, OutputID) VALUES(" + str(value) + ", '" + date + "', " + str(source) + ")")
        writer.execute("UPDATE OUTPUTS_CURRENT SET State = " + str(value) + " WHERE OutputID = " + str(source))

    except Error as e:
        print("Error while putting data in the database")
        print(e)
        raise Exception("Writing to the db")
