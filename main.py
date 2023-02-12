import argparse
import os

from dotenv import load_dotenv

import time

import requests
import json
import csv

import socket

import pandas as pd

# Install theharvester
os.system("./install_theharvester.sh")

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
    parser.add_argument("-u", "--url", type=str,
                        help="Select an to scan")
    parser.add_argument('-i', '--ip', type=str)
    parser.add_argument('-d', '--domain', type=str)
    parser.add_argument('-v', '--vuln', type=str)
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-w', '--wordlist', help='Wordlist file')
    parser.add_argument("-b", "--datasource",
                        help="Data source to use (bing, pgp, linkedin, baidu, dogpile, googleplus, twitter, jigsaw, all)")
    parser.add_argument("-l", "--limit", help="Limit the number of results")
    parser.add_argument("-f", "--file", help="Save the results to a file")

    args = parser.parse_args()

    key = os.getenv("SHODAN_API_KEY")

    # Shodan
    if args.ip and args.domain:
        print("You can't use -i and -d at the same time")

    elif not args.vuln:
        print("You need the amount of vulnérabiltés that you want to see")

    elif args.ip and args.vuln:
        os.system("shodan init " + key)
        os.system("shodan host --save " + args.ip)
        os.system("shodan parse " + args.ip + ".json.gz")
        os.system("shodan convert " + args.ip + ".json.gz csv")
        os.system("rm " + args.ip + ".json.gz")
        os.system("shodan stats --facets vuln:" + args.vuln + " net:" + args.ip + "/24 > vuln_" + args.ip + ".txt")
        print(
            "Toutes les informations sur l'ip ciblé ont été enregistrées dans le fichier " + args.ip + ".csv et toutes ces vulnérabiltés sont enregistrées dans le fichier vuln_" + args.ip + ".txt")

    elif args.domain and args.vuln:
        if args.domain.split(".")[0] == "www":
            domain = socket.gethostbyname(args.domain)
            os.system("shodan init " + key)
            os.system("shodan host --save " + domain)
            os.system("shodan parse " + domain + ".json.gz")
            os.system("shodan convert " + domain + ".json.gz csv")
            os.system("rm " + domain + ".json.gz")
            os.system("shodan stats --facets vuln:" + args.vuln + " net:" + domain + "/24 > vuln_" + domain + ".txt")
            print(
                "Toutes les informations sur l'ip ciblé ont été enregistrées dans le fichier " + domain + ".csv et toutes ces vulnérabiltés sont enregistrées dans le fichier vuln_" + domain + ".txt")
        else:
            domain = socket.gethostbyname("www." + args.domain)
            os.system("shodan init " + key)
            os.system("shodan host --save " + domain)
            os.system("shodan parse " + domain + ".json.gz")
            os.system("shodan convert " + domain + ".json.gz csv")
            os.system("rm " + domain + ".json.gz")
            os.system("shodan stats --facets vuln:" + args.vuln + " net:" + domain + "/24 > vuln_" + domain + ".txt")
            print(
                "Toutes les informations sur l'ip ciblé ont été enregistrées dans le fichier " + domain + ".csv et toutes ces vulnérabiltés sont enregistrées dans le fichier vuln_" + domain + ".txt")

    else:
        print("No arguments")

    # URLScan
    if args.url:
        headers = {'API-Key': os.getenv("URLSCAN_API_KEY"), 'Content-Type': 'application/json'}

        submit_json = URLSCANSubmit(args.url, headers).json()

        result_api = submit_json["api"]
        time.sleep(10)
        r = requests.get(result_api)
        parseJsonInfosFromUrl(r)

    # DNSScan
    domain = args.domain
    output = args.output
    wordlist = args.wordlist

    if not domain:
        print("[-] Please specify a domain name, use --help for more info")
        exit()

    elif domain and not output:
        print("[-] Please specify an output file, use --help for more info")
        exit()

    elif domain and output and not wordlist:
        print("[-] Please specify a wordlist file, use --help for more info")
        exit()

    else:
        print("[+] Starting DNS Scan")
        os.system("./dnscan/dnscan.py -d " + domain + " -w " + wordlist + " -o " + output)

    # theHavester
    if not args.email:
        print("No arguments provided. Use -h for help")

    elif args.email and not args.domain:
        print("No domain provided. Use -h for help")

    elif args.email and args.domain and not args.datasource:
        print("No data source provided. Use -h for help")

    elif args.email and args.domain and args.datasource and not args.limit:
        print("No limit provided. Use -h for help")

    elif args.email and args.domain and args.datasource and args.limit and not args.file:
        print("No file provided. Use -h for help")

    # If all arguments are provided, run theharvester with the arguments and save the results to a file
    elif args.email and args.domain and args.datasource:
        print("Getting emails from " + args.domain + " using " + args.datasource + " data source")
        os.system(
            "cd theHarvester && ./theHarvester.py -d " + args.domain + " -b " + args.datasource + " -l " + args.limit + " -f " + args.file + " && cp " + args.file + ".json ../ && cp " + args.file + ".xml ../")




if __name__ == '__main__':
    load_dotenv()
    parseArgs()