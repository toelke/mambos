"""
Land all drones
"""

from pyparrot.Minidrone import Mambo

# you will need to change this to the address of YOUR mambo
mamboAddr = ["d0:3a:b1:8c:e6:21",
			 "d0:3a:2f:c6:e6:3b",
			 "d0:3a:8a:7e:e6:3b"]


for addr in mamboAddr:

	# make my mambo object
	# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
	mambo = Mambo(addr, use_wifi=False)

	print("trying to connect to %s" % addr)
	success = mambo.connect(num_retries=3)
	print("connected: %s" % success)

	if (success):
		print("landing")
		mambo.safe_land(5)
		print("disconnect")
		mambo.disconnect()
