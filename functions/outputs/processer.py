# Takes the value of an output in the XML code and calls insert_out()
# def out_processer(root, index, multiple, source, writer, date):
def out_processer(root, index, multiple):
    # Index is needed for the research in the file, source is the primary key used to write in the database.
    # Multiple is 0 by default, changed to 1 if the value is in a different location
    try:
        var = root[0][index][1][multiple].text

        if var == "Auto/OFF":
            var = "0"
        if var == "Man/OFF":
            var = "0"
        if var == "OFF":
            var = "0"
        elif var == "Auto/ON":
            var = "1"
        elif var == "Man/ON":
            var = "1"
        elif var == "ON":
            var = "1"
        elif var == "Auto":
            var = out_processer(root, index, 1)

        return var

    except Exception as e:
        print(f"Error while getting the value of outputs: '{e}'")
