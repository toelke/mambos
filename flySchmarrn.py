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
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("taking off!")
    mambo.safe_takeoff(5)
	
    for i in range(3):
        mambo.take_picture()
        print("rolling around!")
        mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=100, duration=1)
        mambo.smart_sleep(1)
        mambo.fly_direct(roll=0, pitch=-200, yaw=0, vertical_movement=0, duration=0.5)
        mambo.smart_sleep(1)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-100, duration=1)
        mambo.smart_sleep(1)

    mambo.smart_sleep(0.5)
	
    print("flip right")
    print("flying state is %s" % mambo.sensors.flying_state)
    success = mambo.flip(direction="right")
    print("mambo flip result %s" % success)
	
    mambo.smart_sleep(0.5)
    # take the photo
    pic_success = mambo.take_picture()

    # need to wait a bit for the photo to show up
    mambo.smart_sleep(0.5)

    picture_names = mambo.groundcam.get_groundcam_pictures_names() #get list of availible files
    print(picture_names)

    frame = mambo.groundcam.get_groundcam_picture(picture_names[0],True) #get frame which is the first in the array


    print("flip front")
    print("flying state is %s" % mambo.sensors.flying_state)
    success = mambo.flip(direction="front")
    print("mambo flip result %s" % success)
	
    print("going front up!")
    mambo.fly_direct(roll=0, pitch=200, yaw=0, vertical_movement=100, duration=1)

