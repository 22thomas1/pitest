from  pycreate2 import Create2
import time

def sen(bot):
  data = bot.get_sensors()
  print(f"{data.distance:4}")

# Create a Create2.
port = "/dev/ttyUSB0"  # where is your serial port?
bot = Create2(port)

# Start the Create 2
bot.start()
bot.full()

print(bot.get_sensors())
sen(bot)
bot.drive_direct(100,100)
time.sleep(1)
sen(bot)
time.sleep(1)
bot.drive_stop()

bot.close()
