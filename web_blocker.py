import time
from datetime import datetime as dt
hosts_temp = "C:\python3\learn\settingup\web_blocker\hosts" #this is the path of the host file which is stored locally for the testing purpose
hosts_path = "c:\Windows\System32\drivers\etc\hosts" # this is original hosts file
redirect = "127.0.0.1"

website_list = ["www.facebook.com","facebook.com","www.linkedin.com/feed/","linkedin.com/feed/"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print ("Working hours....")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    #print ("hello")
                    content1 = file.write(redirect+"    "+ website + "\n")

    else:
        print ("Fun Hours....")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            print ("No problem.....")

    time.sleep(5)
