
#!/usr/bin/env python3


from __future__ import absolute_import, division, print_function

import json
import netmiko
from netmiko import ConnectHandler


JSON_FILE = ""
COMMAND = ""

# Open Json file with hosts, and make it a list 
with open(JSON_FILE) as dev_file:
        devices = json.load(dev_file)


# Error messages
netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)



for device in devices:
    try:
        print('~' * 79)
        # connecting to device
        connector = ConnectHandler(**device)
        hostname = connector.base_prompt
        output = connector.find_prompt()
        print('Connected successfully to device:' + hostname + ' ' , device['ip'])

        #Sending command
        output += connector.send_command(COMMAND, delay_factor=2)
        print(COMMAND + " sent to " + hostname)
        #closing the connection to the device
        connector.disconnect()
    # Error handeling    
    except netmiko_exceptions as e:
        hostname = ''
        print('Failed to ', device['ip'], e)
        