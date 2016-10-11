import sys
from ST_VL6180X import VL6180X
from time import sleep
import RPi.GPIO as GPIO  # Import GPIO functions

"""-- Setup --"""
debug = False
if len(sys.argv) > 1:
    if sys.argv[1] == "debug":  # sys.argv[0] is the filename
        debug = True



# Loop through specified address list to initiate sensor objects
tof_sensor = {} 							# initialize a dictionary
for tof_address in xrange(0x2b,0x2c):
	tof_sensor[tof_address] = VL6180X(address=tof_address, debug=debug)
	# tof_sensor.get_identification()
	# if tof_sensor.idModel != 0xB4:
	#     print"Not a valid sensor id: %X" % tof_sensor.idModel
	# else:
	#     print"Sensor model: %X" % tof_sensor.idModel
	#     print"Sensor model rev.: %d.%d" % \
	#          (tof_sensor.idModelRevMajor, tof_sensor.idModelRevMinor)
	#     print"Sensor module rev.: %d.%d" % \
	#          (tof_sensor.idModuleRevMajor, tof_sensor.idModuleRevMinor)
	#     print"Sensor date/time: %X/%X" % (tof_sensor.idDate, tof_sensor.idTime)
	tof_sensor[tof_address].default_settings()

# # Set output pin numbers for LEDS
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)  # Use GPIO numbering scheme (not pin numbers)
# LED = [17, 27]          # List of GPIOs to use for LED output
# for i in range(len(LED)):
#     GPIO.setup(LED[i], GPIO.OUT)  # Set all as output
#     print("GPIO_%d is output" % LED[i])
#     GPIO.output(LED[i], 0)  # Turn all LEDs off

sleep(1)

"""-- MAIN LOOP --"""
while True:
	for key, value in tof_sensor.iteritems():
		print "Sensor: 0x{:2x} \t Value: {}".format(key, tof_sensor[0x2b].get_distance())
	sleep(1)
