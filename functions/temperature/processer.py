# Takes the value of temperature in the XML code and calls insert_temp()
#def temp_processer(root, index, source, writer, date):
def temp_processer(root, index):
    # Index is needed for the research in the file, source is the primary key used to write in the database.
    try:
        var = root[index][1][0].text
        num = ''
        i=0

        while (var[i] != ' ') or (i == len(var)):
            num = num + str(var[i])
            i = i + 1

        return num
        #insert_temp(num, str(source), writer, date)

    except Exception as e:
        print(f"Error while getting the value of temperature: '{e}'")
