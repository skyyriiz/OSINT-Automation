import os
import argparse

#os.system("./dnscan_installation.sh")

parser = argparse.ArgumentParser(description='DNS Scan')

parser.add_argument('-d', '--domain', help='Domain name', required=True)
parser.add_argument('-o', '--output', help='Output file', required=True)
parser.add_argument('-w', '--wordlist', help='Wordlist file', required=True)

args = parser.parse_args()

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