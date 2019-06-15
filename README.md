# Domotico-casa

This prototype reads data from [Dinergy](https://www.dynergysrl.it) (heating/cooling control system) and Bticino (home automation control system, very experimental).
This allows storing in a database all the data coming from the above systems, showing all the historical data and trends (with Grafana).

The system is not yet flexible enough to be deployed as is in different conditions (e.g., another house); it this case the source code may require some small modifications and adaptations.

Please note that the [Settings.json](Settings.json) file contains some passwords in clear: please make suyre that your system is well protected and not accessible from the outside world.
