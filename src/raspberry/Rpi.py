import RPi.GPIO as GPIO
import smbus2
import time

GPIO.setmode(GPIO.BCM)

class Rpi:
    def __init__(self):
        GPIO.setup(14, GPIO.IN)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)

        self.bus = smbus2.SMBus(1)
        self.address = 0x48
        self.last_joystick_action = time.time()
        self.joystick_delay = 0.2  # Delay in seconds between joystick actions
        self.last_button_action = time.time()
        self.button_delay = 0.3  # Delay in seconds between button actions

    def read_joystick_x(self):
        try:
            self.bus.write_byte(self.address, 0)  # Channel 0 for X-axis
            self.bus.read_byte(self.address)  # Dummy read to start conversion
            return self.bus.read_byte(self.address)
        except OSError as e:
            print(f"I2C communication error: {e}")
            return None

    def read_joystick_y(self):
        try:
            self.bus.write_byte(self.address, 1)  # Channel 1 for Y-axis
            self.bus.read_byte(self.address)  # Dummy read to start conversion
            return self.bus.read_byte(self.address)
        except OSError as e:
            print(f"I2C communication error: {e}")
            return None

    def get_button(self):
        if GPIO.input(14) == 0:
            return True
        return False

    def process_button(self, game):
        current_time = time.time()
        if current_time - self.last_button_action >= self.button_delay:
            if self.get_button():
                game.rotate()  # Rotate the figure
                self.last_button_action = current_time
                return True
        return False

    def process_joystick(self, game):
        current_time = time.time()
        if current_time - self.last_joystick_action >= self.joystick_delay:
            # Read X-axis for left/right movement
            joystick_x = self.read_joystick_x()
            if joystick_x is not None:
                if joystick_x < 100:
                    game.go_side(1)  # Move right
                    self.last_joystick_action = current_time
                elif joystick_x > 225:
                    game.go_side(-1)  # Move left
                    self.last_joystick_action = current_time

            # Read Y-axis for down movement
            joystick_y = self.read_joystick_y()
            if joystick_y is not None:
                if joystick_y < 100:  # Joystick pushed down
                    game.go_down()  # Move block down
                    self.last_joystick_action = current_time

    def reset_game(self):
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)

    def remove_life(self, lives):
        if lives > 0:
            lives -= 1
            if lives == 2:
                GPIO.output(17, GPIO.LOW)
            elif lives == 1:
                GPIO.output(27, GPIO.LOW)
            elif lives == 0:
                GPIO.output(22, GPIO.LOW)