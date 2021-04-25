from  pycreate2 import Create2
import time

# Create a Create2.
RLOR= Create2("/dev/ttyUSB0")


RLOR.start()
RLOR.full()
RLOR.drive_direct(500,500)
time.sleep(0.5)
RLOR.drive_direct(-500,500)
time.sleep(0.5)
RLOR.drive_direct(500,500)
time.sleep(0.5)
RLOR.drive_direct(-500,500)
time.sleep(0.5)
RLOR.drive_direct(500,500)
time.sleep(0.5)
RLOR.drive_direct(-500,500)
time.sleep(0.5)
RLOR.drive_direct(500,500)
time.sleep(0.5)
RLOR.drive_stop()
RLOR.close()
