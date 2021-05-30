#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
'''from opcua import Client, ua
from machines.msg import Pneumatic
import sys
import time


def callback(data):
    client = Client("opc.tcp://10.226.52.91:4840")
    client.connect()


callback()'''

'''
the following import is only necessary because eip.py is not in this directory
'''

'''
import sys
sys.path.append('..')


from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '10.226.52.103'
    tags = comm.GetTagList()
    
    for t in tags.Value:
        print(t.TagName, t.DataType)

'''


import sys
sys.path.append('..')



from pylogix import PLC
import time
#pub = rospy.Publisher('rfid', Int32, queue_size=10)
#rospy.init_node('talker', anonymous=True)
with PLC() as comm:
comm.IPAddress = '10.226.52.103'
    while True:
	    ret = comm.Read('RFID_Tagvalue')
            value = ret.Value
	    print(value)
	    #pub.publish(value)
