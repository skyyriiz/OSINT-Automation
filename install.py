import os

os.system("python -m pip install --upgrade pip")
os.system("pip install python-dotenv")

os.system("git clone https://github.com/rbsec/dnscan.git")
os.system("cd dnscan && sudo pip install -r requirements.txt")
os.system("sudo apt install python3-dnspython")
os.system("cd ..")

os.system("git clone https://github.com/laramies/theHarvester.git")
os.system("cd theHarvester")
os.system("sudo pip3 install -r requirements/dev.txt")
os.system("sudo pip3 install -r requirements/base.txt")
os.system("cd ..")

os.system("python -m pip install --upgrade pip")
os.system("pip install python-dotenv")
os.system("pip install argparse")
os.system("pip install XlsxWriter")