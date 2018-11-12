import time
from datetime import datetime as dt
temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list =["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22,20):
        print("Study")
        with open(host_path,'r+') as myfile:
            content=myfile.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    myfile.write(redirect +" " + website + "\n")                 
    else:
        print("Have Fun!")
        with open(host_path,'r+') as myfile:
            content = myfile.readlines()
            myfile.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    myfile.write(line)
            myfile.truncate()

    time.sleep(5)