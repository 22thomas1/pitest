from  pycreate2 import Create2
import time

# Create a Create2.
port = "/dev/ttyUSB0"  # where is your serial port?
bot = Create2(port)

# Start the Create 2
bot.start()
bot.full()

bot.drive_direct(10,10)
time.sleep(5)
bot.drive_stop()

bot.close()
