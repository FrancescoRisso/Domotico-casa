import xml.etree.ElementTree as ET
import requests
import random

from functions.config import config


def dl_connect():
    configuration = config()
    link = configuration['Datalogger']['ip'] + configuration['Datalogger']['key']
    logout = configuration['Datalogger']['ip'] + configuration['Datalogger']['logout']

    conn_logout = requests.get(logout)
    conn_logout.close()
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
    return conn


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

