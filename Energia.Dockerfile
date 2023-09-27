FROM python:3.10

WORKDIR /domotico-casa

RUN pip install mysql-connector-python requests

COPY Settings.json Settings.json
COPY Energia_elettrica.py Energia_elettrica.py
COPY functions/common functions/common
COPY functions/electricity functions/electricity

ENTRYPOINT [ "python3", "/domotico-casa/Energia_elettrica.py", "/domotico-casa/Energia_elettrica.py" ]
