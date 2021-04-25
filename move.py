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
  return int(f"{data.distance:4}")

def senAngle(bot):
  data = bot.get_sensors()
  return int(f"{data.angle:4}")

def drive(bot,dist,speed):
  if dist==0:
    return None
  if dist<0:  # for driving in reverse
    dist = abs(dist)
    speed = -speed
  
  print("Starting Driving "+dist)
  distanceTravelled=senDistance(bot)
  bot.drive_direct(speed,speed)
  while distanceTravelled<dist*1000:
    distanceTravelled+=senDistance(bot)
    print("Distance Travelled = "+distanceTravelled)
  bot.drive_stop()

def turn(bot,angle,speed):
  if angle==0:
    return None
  wheelTrack = 230  # distance between two wheels (mm)
  travelDistance = abs((angle/360)*(math.pi*wheelTrack))  # (percentage of circle)*(circumference)
  travelTime = travelDistance/speed
  if angle<0:
    angle = abs(angle)
    speed = -speed
  bot.drive_direct(-speed,speed)
  time.sleep(travelTime)
  bot.drive_stop()
  
  
# initializations
RLOR = initBot("/dev/ttyUSB0")
f=open("input.txt","r")
f.readline() #skip instruction line

# global variables
driveSpeed = 100
turnSpeed = 100

for line in f:
  angle,distance = list(map(float,line.split(" ")))
  turn(RLOR,angle,turnSpeed)
  drive(RLOR,distance,driveSpeed)

# cleanup
f.close()
RLOR.close()
