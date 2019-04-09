# coding: latin-1

# Flask example: https://realpython.com/flask-by-example-part-1-project-setup/
from flask import Flask
app = Flask(__name__)

header = '<html><header><title>Home control panel</title></header><body>'
footer = '<hr><p>Last modified: April 9, 2019</p></body></html>'

@app.route('/')
def hello():
    page= header
    page = page + "<h1>Home control panel</h1><hr>"
    page = page + "<p>Hello world!</p>"
    page = page + footer
    return page

if __name__ == '__main__':
# https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
# Note: since port 80 is a privileged port, this program has to be started with root permissions.
    app.run(host= '0.0.0.0', port=80)
#   Default call to this app
#   app.run()
