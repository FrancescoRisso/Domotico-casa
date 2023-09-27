FROM python:3.10

WORKDIR /domotico-casa

RUN pip install mysql-connector-python requests

COPY Settings.json Settings.json
COPY Temperatura.py Temperatura.py
COPY functions/common functions/common
COPY functions/outputs functions/outputs
COPY functions/temperature functions/temperature

ENTRYPOINT [ "python3", "/domotico-casa/Temperatura.py", "/domotico-casa/Temperatura.py" ]
