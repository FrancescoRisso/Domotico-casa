from mysql.connector import Error


# Insert a certain temperature in the database
def insert(values, writer, date, what):
    try:
        DBnames = "Date"
        DBvalues = f"'{date}'"
        for value in values:
            DBnames = f"{DBnames}, {value['name']}"
            DBvalues = f"{DBvalues}, '{value['value']}'"

        writer.execute(f"INSERT INTO {what}({DBnames}) VALUES({DBvalues})")

    except Error as e:
        print(f"Error while putting data in the database: {e}")
