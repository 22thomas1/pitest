from gpiozero import LED
from time import sleep

red=LED(14)

red.on()
sleep(5)
red.off()
sleep(5)
red.on()
sleep(5)
red.off()
sleep(5)
