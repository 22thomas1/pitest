from  pycreate2 import Create2
import time

def sen(bot,id):
  data = bot.get_sensors()
  print(data[id])

# Create a Create2.
port = "/dev/ttyUSB0"  # where is your serial port?
bot = Create2(port)

# Start the Create 2
bot.start()
bot.full()

sen(bot,19)
bot.drive_direct(100,100)
time.sleep(1)
sen(bot,19)
time.sleep(1)
bot.drive_stop()

bot.close()
