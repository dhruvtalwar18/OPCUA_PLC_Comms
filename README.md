# OPCUA_PLC_tests
An implementation of simple python libraries and OPC-UA communication between PLCs of different make.
We have established communication (both read and write access) between:

1. Allen Bradley PLC to Python(Using OPC-UA)
2. Allen Bradley PLC to Python Script(pylogix library)
3. Siemens S7 PLC to Python(Using OPC-UA)

<b><h0>Pre-requirements</h0></b>

1. The linux machine and the PLC should be on the same network. 
2. The IP address or the OPC-UA address should be known.
3. The tags of the sensors or the inputs to the PLC should be known


We need certain libraries before we can run the codes.

Install python-opcua by entering the following commands in the terminal:

$ sudo apt update

$ sudo apt install python-opcua


Install the Rockwell Automation Logix based python Libraries:-

$ sudo apt update

$ pip install pylogix



We can also use the library below, but I have used pylogix for the same.

$ pip install pycomm3


After all the libraries have been installed the codes can be launched in the linux terminal,
E.g

$ python pylogic_python.py 









