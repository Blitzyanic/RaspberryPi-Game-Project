# PCF8591        Raspberry Pi
# --------       ------------
# VCC      <-->  3.3V (Pin 1)
# GND      <-->  GND (Pin 6)
# SDA      <-->  SDA (GPIO 2, Pin 3)
# SCL      <-->  SCL (GPIO 3, Pin 5)
# AIN0     <-->  VRX (Joystick)
# AIN1     <-->  VRY (Joystick Y-axis)


# Raspberry     LED
# ---------     ---
# 34 GND    <-> - Bar
# 11 GPIO17 <-> - LED
# 13 GPIO27 <-> - LED
# 15 GPIO22 <-> - LED
import RPi.GPIO as GPIO
import smbus2
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup for button
GPIO.setup(14, GPIO.IN)


class JoystickTester:
    def __init__(self):
        self.bus = smbus2.SMBus(1)
        self.address = 0x48

    def read_joystick_x(self):
        try:
            self.bus.write_byte(self.address, 0)  # Channel 0 for X-axis
            self.bus.read_byte(self.address)  # Dummy read
            return self.bus.read_byte(self.address)
        except OSError as e:
            print(f"I2C X-axis error: {e}")
            return None

    def read_joystick_y(self):
        try:
            self.bus.write_byte(self.address, 1)  # Channel 1 for Y-axis
            self.bus.read_byte(self.address)  # Dummy read
            return self.bus.read_byte(self.address)
        except OSError as e:
            print(f"I2C Y-axis error: {e}")
            return None

    def read_button(self):
        return GPIO.input(14) == 0


try:
    print("Joystick Test - Press CTRL+C to exit")
    print("--------------------------------")
    tester = JoystickTester()

    while True:
        x_val = tester.read_joystick_x()
        y_val = tester.read_joystick_y()
        button = tester.read_button()

        x_status = "Center"
        if x_val < 100:
            x_status = "LEFT"
        elif x_val > 225:
            x_status = "RIGHT"

        y_status = "Center"
        if y_val < 100:
            y_status = "UP"
        elif y_val > 225:
            y_status = "DOWN"

        print(
            f"X-axis: {x_val} ({x_status}) | Y-axis: {y_val} ({y_status}) | Button: {'PRESSED' if button else 'RELEASED'}")
        time.sleep(0.2)  # Update every 200ms

except KeyboardInterrupt:
    print("\nTest ended by user")
    GPIO.cleanup()