import shodan
import argparse
import os
from dotenv import load_dotenv

parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

parser.add_argument('-i', '--ip')
parser.add_argument('-d', '--domain')

args = parser.parse_args()

api_key = shodan.Shodan("7daDcD0wcDnczyFX2E4jIHoDG41s2iZB");

print(api_key);

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api_key.search('esgi.fr')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
except shodan.APIError as e:
        print('Error: {}'.format(e))
        
# Lookup the host
host = api_key.host('195.25.230.205')

# Print general info
print("""
        IP: {}
        Organization: {}
        Operating System: {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

# Print all banners
for item in host['data']:
        print("""
                Port: {}
                Banner: {}

        """.format(item['port'], item['data']))




