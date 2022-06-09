"""
This file contains Cisco VPN authentication function
"""
import subprocess

def auth_cisco_vpn__(configuration_file):

    # Grab Token
    proc = subprocess.Popen(['stoken', 'tokencode'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    store = list(proc.stdout)
    token = store[0].strip()
  
    # Credentials
     with open(configuration) as configuration:
            config = json.load(configuration)
    username = config['username']
    password = config['password']
    server = config['server']
    # Assign cmd
    credentials = "printf '" + username + "\\n" + password + "\\ny'"
    vpn_cmd = "/opt/cisco/anyconnect/bin/vpn -s connect '" + server + "'"
    cmd = credentials + " | " + vpn_cmd
    
    # Command Execution
    print("Executing Command: \n" + cmd)
    subprocess.Popen(cmd,
                     shell=True,
                     executable="/bin/bash",
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE).communicate()

