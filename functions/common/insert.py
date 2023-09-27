from mysql.connector import Error


# Insert a certain temperature in the database
def insert(values, writer, date, what):
    try:
        DBnames = "Date"
        DBvalues = f"'{date}'"
        DBupdate = ""
        for value in values:
            DBnames = f"{DBnames}, {value['name']}"
            DBvalues = f"{DBvalues}, '{value['value']}'"
            DBupdate = f"{DBupdate}, {value['name']} = {value['value']}"

        writer.execute(f"INSERT INTO {what}({DBnames}) VALUES({DBvalues})")
        if what == "TEMPERATURES":
            writer.execute(f"UPDATE TEMPERATURES_CURRENT SET {DBupdate[2:]} WHERE Id = 1")

    except Error as e:
        print(f"Error while putting data in the database: {e}")
