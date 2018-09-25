#!/usr/bin/env python
import socket
import subprocess
import sys
import platform

from termcolor import colored
from datetime import datetime

# Clear the screen


if (platform.system()=='Linux'):
	subprocess.call('clear', shell=True)
else:
	subprocess.call('clr', shell=True)

print ("*" * 57)
print colored("*\t\tWelcome to Open port Scanner \t\t*","red")
print ("*" * 57)

# Ask for input
remoteServer    = raw_input("..Enter a host address to scan.. \n>>")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan

print ("\nPlease wait, scanning...", remoteServerIP,"\n")


# Check what time the scan started
t1 = datetime.now()


try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()
print '\nStarting Time of Scaning :',t1
print 'Ending Time of Scaning   :',t2


