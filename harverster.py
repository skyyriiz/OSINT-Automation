import os
import argparse
import pandas as pd

# Install theharvester
os.system("./install_theharvester.sh")

# Parse arguments
parser = argparse.ArgumentParser()

# Arguments to get emails from a domain
parser.add_argument("-e", "--email", help="Get emails from a domain")
parser.add_argument("-d", "--domain", help="Domain name to harvest")
parser.add_argument("-b", "--datasource", help="Data source to use (bing, pgp, linkedin, baidu, dogpile, googleplus, twitter, jigsaw, all)")
parser.add_argument("-l", "--limit", help="Limit the number of results")
parser.add_argument("-f", "--file", help="Save the results to a file")


args = parser.parse_args()

# Check if arguments are provided
if not args.email:
    print("No arguments provided. Use -h for help")

elif args.email and not args.domain :
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
    os.system("cd theHarvester && ./theHarvester.py -d " + args.domain + " -b " + args.datasource + " -l " + args.limit + " -f " + args.file + " && cp " + args.file + ".json ../ && cp " + args.file + ".xml ../")

"""
# Not working right now
# Convert the json file to csv
df = pd.read_json(args.file + ".json")
df.to_csv(args.file + ".csv", index=False)
"""



