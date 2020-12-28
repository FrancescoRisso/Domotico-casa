# Packages to be installed

    sudo apt install python3

    sudo apt install python3-pip
    pip3 install mysql-connector-python
    pip3 install requests
    # Python web server
    pip3 install flask
    pip3 install waitress


# To enable the periodic execution of the script

    crontab -e

    SHELL=/bin/bash

    PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

    */5 * * * * python /home/user/Desktop/Domotico-casa/Temperatura.py 1>> /var/log/casa/log 2>> /var/log/casa/error
    0 * * * * python /home/db/Domotico-casa/Energia_elettrica.py 1>> /var/log/casa/log_electricity 2>> /var/log/casa/error_electricity


    // Save upon exit, using the suggested name


# To enable the web server on startup

    https://timleland.com/how-to-run-a-linux-program-on-startup/
