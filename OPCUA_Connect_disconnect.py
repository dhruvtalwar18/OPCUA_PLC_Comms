from opcua import Client, ua
import time

url = "opc.tcp://169.254.4.102:4840"

client = Client(url)
client.connect()
print "CLient connected"


client.disconnect()
print "CLient disconnected"






