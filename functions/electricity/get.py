import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

from functions.electricity.insert import insert


def get(link, writer, day, month, year, hour, config, source):
    data = requests.get(link, auth=HTTPBasicAuth('', config['Datalogger']['password'])).text
    root = ET.fromstring(data.encode('ascii', 'ignore'))

    # Data ahas the following format:
    #<GRAP>
    #  <TYPE>1</TYPE>
    #  <RETCODE>0</RETCODE>
    #  <TOTDAT>225</TOTDAT>
    #  <TOTSLOT>25</TOTSLOT>
    #  <TOTFASC>8</TOTFASC>
    #  <DAT>
    #    <ORDDAT>0</ORDDAT>
    #    <FASCIA>0</FASCIA>
    #    <ORDSLOT>0</ORDSLOT>
    #    <VAL>260</VAL>
    #  </DAT>
    #
    # So, first we have to move to the fifth element, which contains the first measurement ('<DAT>' element).
    # Each measurement has the time kept in the third element ('ORDSLOT').
    # However, there are are 9 measurement in each hour ('FASCIA'), which can be used to differentiate
    # the cost between different timeslots (e.g., night vs day). However, we don't use that.
    # So, we have to read the first measurement in each hour.
    # Consequently, the element we have to read is the 5th (i.e., ORDDAT == 0) for 00:00am,
    # the 14th (i.e., ORDDAT == 9) for 1:00am, the 23rd (i.e., ORDDAT == 18) for 2:00am, and so on.

    i = 5

    try:
        date = "20" + str(year) + "-" + str(month) + "-" + str(day) + "-" + str(hour) + ":00:00"
        # Debug
        # print(link + "     " + str(hour) + " date " + date)

        orddat = 5 + 9 * hour;

        # Debug
        # print (link + " ORDDAT " + str(orddat-5) + " value " + root[orddat][3].text)

        insert(root[i][3].text, source, writer, date)

    except Exception as e:
        print("Error while getting the data: '" + str(e) + "'")

