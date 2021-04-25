from pyparrot.Minidrone import Mambo
import sys

import atexit

# you will need to change this to the address of YOUR mambo
mamboAddrs = ["d0:3a:2f:c6:e6:3b"]

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambos = [Mambo(x, use_wifi=False) for x in mamboAddrs]

for mambo in mambos:
    print("trying to connect")
    success = mambo.connect(num_retries=3)
    print("connected: %s" % success)
    if not success:
        sys.exit(1)


@atexit.register
def land():
    [x.land() for x in mambos]

    print("disconnect")
    [x.disconnect() for x in mambos]


m = mambos[0]
m.drone_connection._safe_ble_write(characteristic=m.drone_connection.ftp_characteristics['NORMAL_FTP_HANDLING'], packet=b'\x03LIS/\x00')
