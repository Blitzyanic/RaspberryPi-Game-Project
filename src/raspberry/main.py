import RPi.GPIO as GPIO
import smbus2

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# PCF8591        Raspberry Pi
# --------       ------------
# VCC      <-->  3.3V (Pin 1)
# GND      <-->  GND (Pin 6)
# SDA      <-->  SDA (GPIO 2, Pin 3)
# SCL      <-->  SCL (GPIO 3, Pin 5)
# AIN0     <-->  VRX (Joystick)

# Set up I2C bus
bus = smbus2.SMBus(1)
address = 0x48  # Address of the PCF8591 ADC module


def read_adc(channel):
    try:
        bus.write_byte(address, channel)
        bus.read_byte(address)  # Dummy read to start conversion
        return bus.read_byte(address)
    except OSError as e:
        print(f"I2C communication error: {e}")
        return None


#try:
#    while True:
#        # Read the analog value from the joystick's VRX pin (channel 0)
#        vrx_value = read_adc(0)
#        if vrx_value is not None:
#            if vrx_value < 100:
#                print("Joystick moved to the left")
#            elif vrx_value > 225:
#                print("Joystick moved to the right")
#            else:
#                print("Joystick is idle")
#        time.sleep(0.1)  # Wait for 100 milliseconds before reading again
#except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
#    GPIO.cleanup()
