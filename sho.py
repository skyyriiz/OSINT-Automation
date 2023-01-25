import shodan
import argparse
import os

parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

parser.add_argument('-i', '--ip', type=str)
parser.add_argument('-d', '--domain', type=str)
parser.add_argument('-v', '--vuln', type=str)

args = parser.parse_args()

api_key = shodan.Shodan("7daDcD0wcDnczyFX2E4jIHoDG41s2iZB");

if args.ip:
        os.system("shodan host --save " + args.ip)
        os.system("shodan parse " + args.ip + ".json.gz")
        os.system("shodan convert " + args.ip + ".json.gz csv")
        os.system("rm " + args.ip + ".json.gz")
        os.system("shodan stats --facets vuln:" + args.vuln + " net:" + args.ip + "/24 > vuln_" + args.ip + ".txt")
        os.system("")
        print("Toutes les informations sur l'ip ciblé ont été enregistrées dans le fichier " + args.ip + ".csv")
        
elif args.domain:
        os.system("shodan host " + args.domain)
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
