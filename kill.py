#Simple script for killing the motors if I forget to stop them

from  pycreate2 import Create2
import time
RLOR= Create2("/dev/ttyUSB0")
RLOR.start()
RLOR.full()
RLOR.drive_stop()
RLOR.close()
