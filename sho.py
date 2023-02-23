import shodan
import argparse
import os
import socket
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

parser.add_argument('-i', '--ip', type=str)
parser.add_argument('-d', '--domain', type=str)
parser.add_argument('-v', '--vuln', type=str)

args = parser.parse_args()

# api_key = shodan.Shodan("7daDcD0wcDnczyFX2E4jIHoDG41s2iZB");

key = os.getenv("SHODAN_API_KEY")

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
        print("Toutes les informations sur l'ip ciblé ont été enregistrées dans le fichier " + args.ip + ".csv et toutes ces vulnérabiltés sont enregistrées dans le fichier vuln_" + args.ip + ".txt")

elif args.domain and args.vuln:
        if args.domain.split(".")[0] == "www":
                domain = socket.gethostbyname(args.domain)
                os.system("shodan init " + key)
                os.system("shodan host --save " + domain)
                os.system("shodan parse " + domain + ".json.gz")
                os.system("shodan convert " + domain + ".json.gz csv")
                os.system("rm " + domain + ".json.gz")
                os.system("shodan stats --facets vuln:" + args.vuln + " net:" + domain + "/24 > vuln_" + domain + ".txt")
                print("Toutes les informations sur l'ip ciblé ont été enregistrées dans le fichier " + domain + ".csv et toutes ces vulnérabiltés sont enregistrées dans le fichier vuln_" + domain + ".txt")
        else:
                domain = socket.gethostbyname("www." + args.domain)
                os.system("shodan init " + key)
                os.system("shodan host --save " + domain)
                os.system("shodan parse " + domain + ".json.gz")
                os.system("shodan convert " + domain + ".json.gz csv")
                os.system("rm " + domain + ".json.gz")
                os.system("shodan stats --facets vuln:" + args.vuln + " net:" + domain + "/24 > vuln_" + domain + ".txt")
                print("Toutes les informations sur l'ip ciblé ont été enregistrées dans le fichier " + domain + ".csv et toutes ces vulnérabiltés sont enregistrées dans le fichier vuln_" + domain + ".txt")

else:
        print("No arguments")







"""
if args.ip:
        host = api_key.host(args.ip)
        print(
        IP: {}
        Organization: {}
        Operating System: {}
        .format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        for item in host['data']:
                print(
                Port: {}
                Banner: {}
                .format(item['port'], item['data']))

elif args.domain:
        print("Domain")

else:
        print("No arguments")
"""
