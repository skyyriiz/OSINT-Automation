import argparse
import os

from dotenv import load_dotenv

import time

import requests
import json
import csv

def URLSCANSubmit(url, headers):
    data = {"url": url, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    return response

def parseJsonInfosFromUrl(req):
    result = req.json()

    os.system("mkdir urlscan && touch urlscan/report.csv")
    row_list = [
        ["Domain", result["page"]['domain']],
        ["Page IP", result["page"]['ip']],
        ["Country", result["page"]['country']],
        ["City", result["page"]['city']],
        ["List of IPs"] + result["lists"]['ips'],
        ["Linked domains"] + result["lists"]['linkDomains'],
        ["Subdomains"] + result["lists"]['domains'],
        #["Technologies used"] + result['meta']['processors']['wappa']['data']
    ]
    with open('urlscan/report.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        writer.writerows(row_list)


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
    parser.add_argument("-u", "--url", type=str,
                        help="Select an to scan")


    args = parser.parse_args()

    if args.email:
        print("infos")
    if args.phone:
        print("infos")
    if args.ip_address:
        print("infos")
    if args.domain_name:
        print("infos")
    if args.url:
        headers = {'API-Key': os.getenv("URLSCAN_API_KEY"), 'Content-Type': 'application/json'}

        submit_json = URLSCANSubmit(args.url, headers).json()

        result_api = submit_json["api"]
        time.sleep(10)
        r = requests.get(result_api)
        parseJsonInfosFromUrl(r)




if __name__ == '__main__':
    load_dotenv()
    parseArgs()