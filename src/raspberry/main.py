import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up GPIO 4 as an input
GPIO.setup(4, GPIO.IN)

try:
    while True:
        # Read the input from GPIO 4
        input_state = GPIO.input(4)
        print(f"GPIO 4 input state: {input_state}")
        time.sleep(1)  # Wait for 1 second before reading again
except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()