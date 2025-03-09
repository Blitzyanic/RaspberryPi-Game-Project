import gpiod

# Define the chip and line
chip = gpiod.Chip('gpiochip0')
line = chip.get_line(21)

# Request the line as an input
line.request(consumer='read', type=gpiod.LINE_REQ_DIR_IN)

# Read the value from GPIO pin 21
value = line.get_value()

print(f'GPIO pin 21 value: {value}')