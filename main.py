#import os
import argparse
from dotenv import load_dotenv

import requests


def searchFromPhoneNumber(phone_number):
    url = 'https://www.telephoneannuaire.fr/search'
    post_obj = {'r_who': phone_number}
    response = requests.post(url, data=post_obj)
    print(response.content)

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

    if args.email:
        # api-endpoint
        url = "https://haveibeenpwned.com/unifiedsearch"


        param = {'email': args.email}


        r = requests.get(url=url, params=param)
        print(r.json())
    if args.phone:
        searchFromPhoneNumber(args.phone)

    if args.ip_address:
        print("infos")
    if args.domain_name:
        print("infos")





if __name__ == '__main__':
    load_dotenv()
    parseArgs()

