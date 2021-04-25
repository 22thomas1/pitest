from  pycreate2 import Create2
import time
import math

# functions
def initBot(port):
  bot = Create2(port)
  bot.start()
  bot.full()
  return bot

def drive(bot,dist,speed):
  if dist==0:
    return None
  travelTime = dist*1000/speed
  if dist<0:  # for driving in reverse
    dist = abs(dist)
    speed = -speed
  bot.drive_direct(speed,speed)
  time.sleep(travelTime)
  bot.drive_stop()

def turn(bot,angle,speed):
  if angle==0:
    return None
  wheelTrack = 240  # distance between two wheels (mm)
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
driveSpeed = 200
turnSpeed = 200

for line in f:
  angle,distance = list(map(int,line.split(" ")))
  turn(RLOR,angle,turnSpeed)
  drive(RLOR,distance,driveSpeed)

# cleanup
f.close()
RLOR.close()
