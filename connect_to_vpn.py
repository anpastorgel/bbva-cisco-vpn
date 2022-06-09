from cisco-vpn-authentication.py import auth_cisco_vpn__
import argparse

if __name__ == '__main__':

   parser = argparse.ArgumentParser(description='Given the configuration.json file connect to Cisco VPN')
   parser.add_argument('-configuration,'--configuration_file',help='input configuration file name', required=True)
   args = vars(parser.parse_args())
   configuration_file = args['configuration']
   connect = auth_cisco_vpn__(configuration_file)
