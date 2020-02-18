import xml.etree.ElementTree as ET
import requests
import random
import time

from functions.config import config


def dl_connect(date):
    configuration = config()

    try:
        # For some strange reasons, the datalogger sometimes does not return the proper page
        # unless you connect to the webroot object. Upon this, pages are correctly returned.
        # So, we connect to the webroot obhect, wait for a while, close the connection, 
        # then ask for exactly the object we are interested in.
        link = configuration['Datalogger']['ip']

        print(date + " Connecting to " + link)
        conn = requests.get(link)
        conn.close()

        # Sleep for 5 seconds to see if the datalogger wakes up
        time.sleep(5);

        # Now, ask for the object we are really interested in.
        link = configuration['Datalogger']['ip'] + configuration['Datalogger']['key']

        print(date + " Connecting to " + link)
        conn = requests.get(link)

        key = str(conn.text)
        key = key[5:29]

        i = ConvertiChiave(key)
        d = configuration['Datalogger']['password']
        l = 1
        o = Calcola(d,i)
        W1 = o[0:24]
        W2 = o[24:48]

        link = configuration['Datalogger']['ip'] + configuration['Datalogger']['key_send'] + "?W1=" + W1 + "&W2=" + W2
        conn = requests.get(link)

        print(date + " Connecting to " + link)
        print(date + " Answer: " + str(conn.status_code) + " " + conn.reason)
        # print(date + " Returned page: " + conn.text)

        return conn

    except Exception as e:
        print(date + " Unable to connect to the datalogger (" + link + "): '" + str(e) + "'")
        quit()


def ConvertiChiave(e):
    t = ""
    n = e[0]
    n = int(n)
    i = e[n-1]
    i = int(i)
    for d in range(0, 24):
        if not(24 > i + d):
            l = 24 - d
            break
        t += e[i+d]

    for d in range(0, l):
        t += e[d]
    return t


def Calcola(e, t):
    l=''
    i=[]
    d=[]
    n=[]
    for o in range(0, 12):
        n = n + [int(t[2*o:2*o+2], 16)]
    for o in range(0, len(e)):
        i = i + [ord(e[o])]
    for o in range(len(e), 12):
        i = i + [random.randint(0, 40)]
    for o in range(0, 12):
        d = d + [int(i[o]) * int(n[o])]
        s = hex(d[o]).lstrip('0x')
        while len(s) < 4:
            s = "0" + s
        l += s
    return l

