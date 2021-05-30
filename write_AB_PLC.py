import sys
sys.path.append('..')


'''
The simplest example of writing a tag from a PLC
NOTE: You only need to call .Close() after you are done exchanging
data with the PLC.  If you were going to read/write in a loop or read/write
more tags, you wouldn't want to call .Close() every time.
'''
from pylogix import PLC
comm = PLC()
comm.IPAddress = '10.226.52.103'
comm.Write('Tag name', 'Value')
comm.Close()
