Bedroom Environment Monitor (Raspberry Pi + Sense HAT)



Overview:



This project reads temperature and humidity from the Sense HAT on a Raspberry Pi.

The data is then sent to Blynk and ThingSpeak so it can be seen live and also stored.

There is also some simple logic to check if the values go over a certain level and trigger alerts.



What it does:

* Reads temp + humidity from Sense HAT
* Sends values to Blynk dashboard
* Sends values to ThingSpeak using HTTP
* Triggers alerts when thresholds are hit
* LED flashes on the Sense HAT depending on threshold met



Tech used:

* Python
* Sense HAT
* Blynk
* ThingSpeak
* HTTP requests



How to run it

* cd \~/bedroom-environment-monitor
* source .venv/bin/activate
* python blynk.py



How it works:

* The Sensor reads data
* Python checks if values are too high
* Sends data over network (Blynk + HTTP)
* Output shows on dashboards + LED + notifications
* Layers (assignment requirement)
* Data Source → Sense HAT
* Processing → Python logic (threshold checks)
* Network → Blynk + HTTP (ThingSpeak)
* Application → dashboards, alerts, LED display



Notes:

Temp and humidity thresholds were adjusted during testing so the correct LED colour could be clearly seen flashing in the demo as both couldn't flash at the same time.

Temp threshold is set quite low so it triggers easily.

ThingSpeak needs 15 seconds delay or it wont update properly.



Youtube Link: https://youtu.be/WRQSqaGC4hg

