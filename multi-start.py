"""
Demo the direct flying for the python interface

Author: Amy McGovern
"""

from pyparrot.Minidrone import Mambo
import sys

import atexit

# you will need to change this to the address of YOUR mambo
mamboAddrs = ["d0:3a:2f:c6:e6:3b", "d0:3a:b1:8c:e6:21"]

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambos = [Mambo(x, use_wifi=False) for x in mamboAddrs]


def callback(mambo):
    print(
        f"Battery: {mambo.sensors.battery} SpeedXYZTs: {mambo.sensors.speed_x:0.2f},{mambo.sensors.speed_y:0.2f},{mambo.sensors.speed_z:0.2f},{mambo.sensors.speed_ts:0.2f} Flying State: {mambo.sensors.flying_state}"
    )


for mambo in mambos:
    print("trying to connect")
    success = mambo.connect(num_retries=3)
    print("connected: %s" % success)
    if not success:
        sys.exit(1)


@atexit.register
def land():
    [x.land() for x in mambos]


[x.set_user_sensor_callback(callback, x) for x in mambos]


print("taking off!")
[x.takeoff() for x in mambos]
mambos[0].smart_sleep(2)

print("landing")
[x.land() for x in mambos]
mambos[0].smart_sleep(2)

print("disconnect")
[x.disconnect() for x in mambos]
