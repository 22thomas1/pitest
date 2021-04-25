#Simple script for killing the motors if I forget to stop them

from  pycreate2 import Create2
import time
RLOR= Create2("/dev/ttyUSB0")
RLOR.start()
time.sleep(1)
RLOR.full()
time.sleep(1)
RLOR.drive_stop()
time.sleep(1)
RLOR.close()
