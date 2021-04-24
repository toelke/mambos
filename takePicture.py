"""
Demo the direct flying for the python interface

Author: Amy McGovern
"""

import atexit



from pyparrot.Minidrone import Mambo

# you will need to change this to the address of YOUR mambo
mamboAddr = "d0:3a:b1:8c:e6:21"

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)


@atexit.register
def safe_land():
    
    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)
    mambo.safe_emergency(5)

    print("disconnect")
    mambo.disconnect()

if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("taking off!")
    mambo.safe_takeoff(5)
    mambo.smart_sleep(2)
	
    mambo.take_picture()

    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

    print("disconnect")
    mambo.disconnect()

