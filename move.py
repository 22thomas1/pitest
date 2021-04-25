from  pycreate2 import Create2
import time
import math

# functions
def initBot(port):
  bot = Create2(port)
  bot.start()
  bot.full()
  return bot

def senDistance(bot):
  data = bot.get_sensors()
  return abs(int(f"{data.distance:4}"))

def senAngle(bot):
  data = bot.get_sensors()
  return abs(int(f"{data.angle:4}"))

def drive(bot,dist,speed):
  if dist==0:
    return None
  if dist<0:  # for driving in reverse
    dist = abs(dist)
    speed = -speed
  print("Starting Driving "+str(dist))
  distanceTravelled=senDistance(bot)
  bot.drive_direct(speed,speed)
  while distanceTravelled<dist*1000:
    distanceTravelled+=senDistance(bot)
  bot.drive_stop()
  print("Distance Travelled = "+str(distanceTravelled))

def turn(bot,angle,speed):
  if angle==0:
    return None
  if angle<0:
    angle = abs(angle)
    speed = -speed
  print("Starting Turning "+str(angle))
  angleTravelled=senAngle(bot)
  bot.drive_direct(-speed,speed)
  while angleTravelled<angle:
    angleTravelled+=senAngle(bot)
  bot.drive_stop()
  print("Angle Travelled = "+str(angleTravelled))
  
# initializations
RLOR = initBot("/dev/ttyUSB0")
f=open("input.txt","r")
f.readline() #skip instruction line

# global variables
driveSpeed = 500
turnSpeed = 500

for line in f:
  angle,distance = list(map(float,line.split(" ")))
  turn(RLOR,angle,turnSpeed)
  drive(RLOR,distance,driveSpeed)

# cleanup
f.close()
RLOR.close()
