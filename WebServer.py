# coding: latin-1

# Flask example: https://realpython.com/flask-by-example-part-1-project-setup/
from flask import Flask
from waitress import serve

app = Flask(__name__)

from functions.date import get_date
from functions.connect import connect

header = '<html>\n\t<header>\n\t\t<title>\n\t\t\tHome control panel\n\t\t</title>\n\t</header>\n\n\t<body>\n\t\t'
footer = '\n\n\t\t<small>\n\t\t\tLast modified: April 28, 2019\n\t\t</small>\n\t</body>\n</html>'


# Read a certain temperature from the database
def read(index):
    reader.execute("SELECT Temperature FROM CURRENT_DATA WHERE InputID = " + str(index))
    var = str(reader.fetchone()).replace("(Decimal('", "").replace("'),)","")
    return var


def page_add(page, stanza, temp):
    page = page + "\n\t\t\t\t<tr>\n\t\t\t\t\t<td>" + stanza + "</td>\n\t\t\t\t\t<td>" + temp + "</td>\n\t\t\t\t</tr>"
    return page



@app.route('/')
def hello():
    page = header
    page = page + "\n\t\t<h1>\n\t\t\tTemperature " + get_date() + "\n\t\t</h1>\n\t\t<hr>"
    page = page + "\n\n\t\t<table>\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th align = \"left\">Stanza</th>\n\t\t\t\t\t<th align = \"left\">Temperatura</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>"
    page = page_add(page, "Camera Francesco", read(1))
    page = page_add(page, "Camera Valentina", read(2))
    page = page_add(page, "Camera Genitori", read(5))
    page = page_add(page, "Studio", read(4))
    page = page_add(page, "Salone", read(3))
    page = page + "\n\t\t\t</tbody>\n\t\t</table>\n\t\t<hr>\n\t\t<p>Per vedere il grafico con gli storici di tutte le temperature <a href =\"https://frisso.grafana.net/d/ri1HUveiz/stanze?orgId=1&refresh=5m&from=now-6h&to=now\">clicca qui</a><hr>"
    page = page + footer
    return page


if __name__ == '__main__':
# https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
# Note: since port 80 is a privileged port, this program has to be started with root permissions.
    host_url = "192.168.0.2"
    db = "Temperatures"
    usr = "prova"
    pwd = "prova"

    date = get_date()
    connection = connect(date, "Temperatures")
    reader = connection.cursor()

serve(app)
    #app.run(host= '0.0.0.0', port=80)
#   Default call to this app
#   app.run()
