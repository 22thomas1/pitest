from  pycreate2 import Create2
import time

# Create a Create2.
port = "/UART0/ttyAMA0"  # where is your serial port?
bot = Create2(port)

# Start the Create 2
bot.start()
bot.full()
bot.close()
