from opcua import Client, ua
import time

url = "opc.tcp://10.226.52.91:4840"

client = Client(url)
client.connect()
print "CLient connected"

distance_sensor = client.get_node('ns=3;s="Distance_Station"')
cam = client.get_node('ns=3;s="Camera_Station"')
rfid = client.get_node('ns=3;s="RFID_Station"')
sol = client.get_node('ns=3;s="Solenoid_Station"')
ext = client.get_node('ns=3;s="Tag_3"')


while True:
	time.sleep(1)
	print "\n\nDis",distance_sensor.get_value()
	time.sleep(1)
	print "cam",cam.get_value()
	time.sleep(1)
	print "rfid",rfid.get_value()
	time.sleep(1)
	print "sol",sol.get_value()
	time.sleep(1)
	print "ext",ext.get_value()
	time.sleep(1)
	

client.disconnect()
print "CLient disconnected"






