import os
import argparse
from dotenv import load_dotenv

def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--email", type=str,
                        help="Select an email to search")
    parser.add_argument("-p", "--phone", type=str,
                        help="Select a phone number to search")
    parser.add_argument("-ip", "--ip_address", type=str,
                        help="Select an ip to search")
    parser.add_argument("-dn", "--domain_name", type=str,
                        help="Select a domain name to search")


    args = parser.parse_args()
    
    match args:
        case args.email:
            print("infos")
        case args.phone:
            print("infos")
        case args.ip:
            print("infos")
        case args.domain_name:
            print("infos")




if __name__ == '__main__':
    load_dotenv()
    parseArgs()

