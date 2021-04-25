from  pycreate2 import Create2
import time

# Create a Create2.
port = "/dev/ttyUSB0"  # where is your serial port?
bot = Create2(port)

# Start the Create 2
bot.start()
bot.full()

bot.drive_direct(100,100)
time.sleep(1)
for x in bot.get_sensors():
  print(x)
time.sleep(1)
bot.drive_stop()

bot.close()
