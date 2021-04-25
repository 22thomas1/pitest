from  pycreate2 import Create2
import time
import math

def sen(bot):
  data = bot.get_sensors()
  return int(f"{data.angle:4}")

# Create a Create2.
port = "/dev/ttyUSB0"  # where is your serial port?
bot = Create2(port)

# Start the Create 2
bot.start()
bot.full()

#print(bot.get_sensors())

angle=90
travelDistance = abs((angle/360)*(math.pi*233))

ang = sen(bot)
bot.drive_direct(-100,100)
while ang<travelDistance:
  ang+=sen(bot)
  print(ang)
bot.drive_stop()


bot.close()
