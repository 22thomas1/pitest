from  pycreate2 import Create2
import time
import math

# Create a Create2.
RLOR = initBot("/dev/ttyUSB0")
driveSpeed = 200
turnSpeed = 200





def initBot(port):
  bot = Create2(port)
  bot.start()
  bot.full()
  return bot

def drive(bot,dist,speed):
  travelTime = dist*1000/speed
  if dist<0:  # for driving in reverse
    dist = abs(dist)
    speed = -speed
  bot.drive_direct(speed,speed)
  time.sleep(travelTime)
  bot.drive_stop()

def turn(bot,angle,speed):
  wheelTrack = 233  # distance between two wheels (mm)
  travelDistance = (angle/360)*(math.pi*wheelTrack)  # (percentage of circle)*(circumference)
  travelTime = travelDistance/speed
  bot.drive_direct(-speed,speed)
  time.sleep(travelTime)
  bot.drive_stop()

RLOR.close()
