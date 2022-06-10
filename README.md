# BBVA - Cisco VPN connection tools
These scripts allows you to connect to the Cisco VPN in a fast and easy way.

## Content

In this repo you will find some useful scripts to connect to Cisco VPN.

### cisco-vpn-authentication.py

It contains a function that allows you to authenticate against the VPN. It needs a configuration file containing the credentials. 

### connect_to_vpn.py

It asks for the configuration file and uses the previous function to connect to Cisco VPN. 

### configuration-template.json

A template of the configuration file. Fill the gaps with the credentials given by the sysadmin.

## Let´s see with an example!

When you call the script you have to pass the configuration file by using -configuration option.

```
python3 connect_to_vpn.py -configuration configuration.json
```


