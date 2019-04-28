from functions.outputs.insert import insert_out


# Takes the value of an output in the XML code and calls insert_out()
def out_processer(root, index, multiple, source, writer, date):
    # Index is needed for the research in the file, source is the primary key used to write in the database.
    # Multiple is 0 by default, changed to 1 if the value is in a different location
    try:
        var = root[0][index][1][multiple].text

        if var == 'Auto/OFF': var = '0'
        if var == 'Man/OFF': var = '0'
        if var == 'OFF': var = '0'
        elif var == 'Auto/ON': var = '1'
        elif var == 'Man/ON': var = '1'
        elif var == 'ON': var = '1'
        elif var == 'Auto':
            out_processer(root, index, 1, source, writer, date)
            return

        insert_out(var, source, writer, date)

    except Exception as e:
        if e == "Writing to the db":
            raise Exception("Writing to the db pt.2")
        else:
            print("Error while getting the value of outputs: '" + str(e) + "'")

