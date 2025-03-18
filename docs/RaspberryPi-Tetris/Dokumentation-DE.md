# **Raspberry-Pi Tetris Projekt**

<div style="page-break-after: always;"></div>

## *Inhalt*

\- [S. 3] ------------ ( _Aufbau_ ) ------------
- **benötigte Materialien**
- **Aufsetzen des Raspberry Pi**
- **Einrichtung des Betriebssystems**
- **Aufbau des Raspberry Pi**


\- [S. 8] ----- ( _Starten des Projektes_ ) ----
- **Klonen des Projektes**
- **Umgang mit der Virtuellen Umgebung**


\- [S. 9] ----- ( _einblick in den Code_ ) -----
- **Projekt Struktur**
- **Beschreibung der Inhalte**

<div style="page-break-after: always;"></div>

## *Aufbau*

### benötigte Materialien
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

schließe Tastatur, Maus und Monitor an den Raspberry an und stecke die Micro-SD Karte ein

<div style="page-break-after: always;"></div>

### Einrichtung des Betriebssystems
wenn sie sich im Raspberry Pi OS befindest, rufe das Terminal auf und updaten sie ihr System
```sh
sudo apt update
sudo apt upgrade

```

nun installiere die Notwendigen Pakete:
```sh
sudo apt install python3 python3-virtualenv
```

jetzt müssen sie nur noch I2C auf den Raspberry Aktivieren
rufe die raspberry pi config TUI auf
```sh
sudo raspi-config
```

nun wähle zuerst **Interface Options** aus und dann I2C und aktiviere es

führen sie nun ein neustart durch
```sh
sudo reboot
```

<div style="page-break-after: always;"></div>

### Aufbau des Raspberry Pi
![[rpi4_pins.png]]
1. Breadboard
- **Pin 6 (GND)** → Minus-Schiene des Breadboards  
- jede **LED** hat eine Verbindung zur **Minus-reihe**
- der **Joystick** (GND-Pin) hat eine Verbindung zur **Minus-reihe**
- das **Button-Modul** (Minus Pin) hat eine Verbindung zur **Minus-reihe**
- das **PCF8591** (GND Pin) Modul hat eine Verbindung zur **Minus-reihe**

<div style="page-break-after: always;"></div>


1. LEDs anschließen (GPIO Output)

| LED   | Raspberry Pi GPIO-Pin |
| ----- | --------------------- |
| LED 1 | GPIO 17 (Pin 11)      |
| LED 2 | GPIO 27 (Pin 13)      |
| LED 3 | GPIO 22 (Pin 15)      |


- Jede LED benötigt einen **220 Ω Widerstand** vor **GND**.

3. PCF8591 anschließen

| PCF8591 Pin | Raspberry Pi Pin |
| ----------- | ---------------- |
| **VCC**     | 3.3V (Pin 1)     |
| **SDA**     | GPIO 2 (Pin 3)   |
| **SCL**     | GPIO 3 (Pin 5)   |

4. Joystick an den PCF8591 anschließen

| Joystick Pin      | PCF8591 Pin |
| ----------------- | ----------- |
| **VRX (X-Achse)** | AIN0 (A0)   |
| **VRY (Y-Achse)** | AIN1 (A1)   |

| Joystick Pin | Raspberry Pi Pin    |
| ------------ | ------------------- |
| **VCC**      | 3.3V (Pin 1)        |

am ende sollte es wie folgt aussehen
![[gpioPins.png]]


<div style="page-break-after: always;"></div>

## *Starten des Projektes*

um mit den Projekt zu beginnen solltest du zuerst das Projekt auf deinen Raspberry Pi klonen

```sh
git clone https://github.com/Blitzyanic/RaspberryPi-Game-Project.git
```

nun gehe in das Projekt erstelle ein virtuelles environment und installiere die Pakete

_wechsel zum Projekt_
```sh
cd RaspberryPi-Game-Project
```

_erstellen eines venv_
```sh
python -m venv .venv
```

_starten des venv_
```sh
source .venv/bin/activate
```

_Installation der Pakete_
```sh
pip install -r requirements.txt
```

_Projekt Starten_
```sh
python src/main.py
```

es sollte sich nun ein Fenster öffnen die Fallenden Blöcke können mit den Joystick bewegt werden und mit den Knopf ist es möglich diese zu drehen

wenn sie die decke erreichen verlieren sie ein Leben (Lampe geht aus)

wenn alle leben verbraucht sind können sie mit ein druck auf den Knopf das spiel neustarten


<div style="page-break-after: always;"></div>

## *Einblick in den Code*
### Projekt Struktur
**.**
├── **docs**  
│  
├── *LICENSE*  
├── main.py  
├── *README.md*  
├── requirements.txt  
└── **src**  
    ├── **game**  
    │   ├── Figure.py  
    │   └── Tetris.py  
    └── **raspberry**  
        └── Rpi.py  

### Beschreibung der Inhalte
- **docs/** → Beinhaltet die Dokumentation wie diese hier 📄  
- **LICENSE** → Das Projekt läuft unter der GPL v3 Lizenz 🔓  
- **main.py** → Hauptdatei des Projekts, verbindet das Tetris-Spiel mit dem Raspberry Pi 🎮🔌  
- **README.md** → Einführung & Infos zum Projekt 📘  
- **requirements.txt** → Enthält die benötigten Python-Pakete mit Versionen 📦  
- **src/** → Quellcode des Projekts 🛠️  
  - **game/** → Enthält den Code für das Tetris-Spiel 🎲  
    - **Figure.py** → Klasse für die Tetris-Blöcke 🧩  
    - **Tetris.py** → Enthält die Spiellogik 🎯  
  - **raspberry/** → Enthält den Code zur Steuerung des Raspberry Pi 🍓  
    - **Rpi.py** → Klasse zum Auslesen der Raspberry-Module 📡  
