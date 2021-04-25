from gpiozero import LED
from time import sleep

red=LED(14)

for x in range(2):
  red.on()
  sleep(1)
  red.off()
  sleep(1)

red.on()
sleep(15)
red.off()
