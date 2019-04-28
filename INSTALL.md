# Packages to be installed

    sudo apt install python

    sudo apt install python-pip
    pip install mysql-connector-python
    pip install requests
    # Python web server
    pip install flask


# To enable the periodic execution of the script

    crontab -e

    SHELL=/bin/bash

    PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

    */5 * * * * python /home/user/Desktop/Domotico-casa/Temperatura.py 1>> /var/log/casa/log 2>> /var/log/casa/error


    // Save upon exit, using the suggested name


# To enable the web server on startup

    https://timleland.com/how-to-run-a-linux-program-on-startup/
