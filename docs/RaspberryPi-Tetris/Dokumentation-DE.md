# **Raspberry-Pi Tetris Projekt**

# *Inhalt*

<div style="page-break-after: always;"></div>
# *Aufbau*

### Materiallien
die Folgenden Gegenstände werden benötigt:
- Raspberry Pi 4 Model B
- Micro-SC Karte mit Raspberry Pi OS
- Breadboard
- 3x Led
- 3x 220 resistor
- Jump-Wires
- Knopf-Modul
- Joystick-Modul
- PCF8591 ADC-Modul
- HDMI-Micro HDMI Kabel
- USB-C Kabel
- Maus
- Tastatur
- Monitor

<div style="page-break-after: always;"></div>

###  Aufsetzen des Raspberry

Lade den <a href="https://www.raspberrypi.com/software/"> Raspberry-Pi Imager </a> herunter 
1. wähle bei Raspberry Pi Modell: **Raspberry Pi 4** aus
2. wähle bei Betriebssystem (OS): **Raspberry Pi OS (64-Bit)** aus
3. wähle deine micro-SD Karte aus und schreibe diese

schließe Tastatur, Maus und Monitor an den Raspberry an und stecke die Micro-SD Karte rein

<div style="page-break-after: always;"></div>

### Einrichtung des Betriebssystems
wenn sie sich im Raspberry Pi OS befindest, rufe das Terminal auf und update dein System
$ *sudo apt update*
$ *sudo apt upgrade*
<br>
nun installiere die Notwendigen Pakete:
$ *sudo apt install python3 python3-virtualenv*

jetzt müssen sie nur noch I2C auf den Raspberry Aktivieren
rufe die raspberry pi config TUI auf
$ *sudo raspi-config*

nun wähle zuerst **Interface Options** aus und dann I2C und aktiviere es

führen sie nun ein neustart durch
$ *sudo reboot*

<div style="page-break-after: always;"></div>

