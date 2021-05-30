from pylogix import PLC
with PLC() as comm:
    comm.IPAddress = '10.226.52.103'
    ret = comm.Read('MyTagName')
    print(ret.TagName, ret.Value, ret.Status)
